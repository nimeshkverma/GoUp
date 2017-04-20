from django.conf import settings
from common.v1.utils.finance_utils import LoanCalculator
from analytics.v1.services import algo360_service, credit_service
from social.models import Login
from loan_product.models import LoanProduct, Loan, PRE_PROCESS
from analytics.models import Algo360
from aadhaar.models import Aadhaar, EKYC
from participant.models import Borrower, Lender

from eligibility_service_constants import LOAN_INTEREST_RATE, LOAN_PROCCESSING_FEES, LOAN_PENALTY_RATE_PER_TENURE
from activity.model_constants import (ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE,
                                      ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE,)


SWASTIKA = 'Swastika'


class CustomerPreLoanProccesing(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.__store_algo360_data()
        self.customer_state = ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE
        self.customer_credit_limit = credit_service.CustomerCreditLimit(
            self.customer_id).limit
        self.loan_interest_rate = None
        self.loan_processing_fee = None
        self.loan_tenure = None
        self.loan_amount = None
        self.loan_emi = None
        self.__assign_loan_attributes()
        self.__determine_customer_eligibility_state()
        self.__pre_loan_processing()

    def __store_algo360_data(self):
        algo360_data = {}
        login_objects = Login.objects.filter(customer_id=self.customer_id)
        if login_objects:
            # imei = '864238035122424'
            imei = login_objects[0].imei
            customer_data = {
                'imei': imei,
                'customer_id': self.customer_id,
            }
            algo360 = algo360_service.Algo360(imei)
            # algo360 = algo360_service.Algo360(self.validated_data.get('customer_id'))
            algo360_data.update(algo360.get_model_data())
            algo360_objects = Algo360.objects.filter(
                customer_id=self.customer_id)
            if algo360_objects:
                Algo360.objects.filter(
                    customer_id=self.customer_id).update(**algo360_data)
                algo360_data.update(customer_data)
            else:
                algo360_data.update(customer_data)
                Algo360.objects.create(**algo360_data)

    def __loan_interest_rate(self):
        self.loan_interest_rate = LOAN_INTEREST_RATE['default']

    def __loan_processing_fee(self):
        nsdl_status = 'nsdl_failed'
        aadhaar_objects = Aadhaar.objects.filter(customer_id=self.customer_id)
        if aadhaar_objects:
            if aadhaar_objects[0].first_name_source == EKYC or aadhaar_objects[0].last_name_source == EKYC:
                nsdl_status = 'nsdl_success'
        loan_processing_fee = self.loan_amount * 1.0 * \
            LOAN_PROCCESSING_FEES[nsdl_status]['principal_percent'] / 100
        loan_processing_fee = max(
            loan_processing_fee, LOAN_PROCCESSING_FEES[nsdl_status]['minimum'])
        loan_processing_fee = min(
            loan_processing_fee, LOAN_PROCCESSING_FEES[nsdl_status]['maximum'])
        self.loan_processing_fee = loan_processing_fee

    def __loan_product_attributes(self):
        loan_product_objects = LoanProduct.objects.filter(
            customer_id=self.customer_id)
        if loan_product_objects:
            self.loan_tenure = loan_product_objects[0].loan_tenure
            self.loan_amount = loan_product_objects[0].loan_amount
            self.loan_emi = LoanCalculator(
                self.loan_amount, self.loan_interest_rate).loan_emi_ceiled(self.loan_tenure)

    def __assign_loan_attributes(self):
        self.__loan_interest_rate()
        self.__loan_product_attributes()
        self.__loan_processing_fee()

    def __update_loan_product_model(self):
        data = {
            'loan_tenure': self.loan_tenure,
            'loan_emi': self.loan_emi,
        }
        LoanProduct.objects.filter(customer_id=self.customer_id).update(**data)

    def __tune_loan_product_attributes(self):
        loan_calculator = LoanCalculator(
            self.loan_amount, self.loan_interest_rate)
        tuned_tenure = loan_calculator.loan_tenure_ceiled(
            self.customer_credit_limit)
        tuned_emi = loan_calculator.loan_emi_ceiled(tuned_tenure)
        self.loan_tenure = tuned_tenure
        self.loan_emi = tuned_emi

    def __determine_customer_eligibility_state(self):
        if self.customer_credit_limit < self.loan_emi:
            self.__tune_loan_product_attributes()

        if self.customer_credit_limit >= self.loan_emi:
            self.customer_state = ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE
            self.__update_loan_product_model()

    def __create_borrower(self):
        data = {
            'customer_id': self.customer_id,
            'credit_limit': self.customer_credit_limit,
            'number_of_active_loans': 0,
            'number_of_repaid_loans': 0,
            'total_current_debt': 0,
            'eligible_for_loan': True,

        }
        Borrower.objects.create(**data)

    def __create_loan(self):
        data = {
            'customer_id': self.customer_id,
            'lender_id': Lender.objects.get(name__iexact=SWASTIKA).id,
            'loan_amount_applied': self.loan_amount,
            'processing_fee': self.loan_processing_fee,
            'tenure': self.loan_tenure,
            'interest_rate_per_tenure': self.loan_interest_rate,
            'penalty_rate_per_tenure': LOAN_PENALTY_RATE_PER_TENURE,
            'status': PRE_PROCESS,
        }
        Loan.objects.create(**data)

    def __pre_loan_processing(self):
        if self.customer_state == ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE:
            self.__create_borrower()
            self.__create_loan()
