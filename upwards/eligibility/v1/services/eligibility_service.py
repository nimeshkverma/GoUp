from django.conf import settings
from social.models import Login
from loan_product.models import LoanProduct
from analytics.v1.services import algo360_service, credit_service
from analytics import models
from customer.v1.service.homepage_config import LOAN_CONSTANTS
from common.v1.utils.finance_utils import LoanCalculator
from activity.models import register_customer_state
from activity.model_constants import (ELIGIBILITY_SUBMIT_STATE,
                                      ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE,
                                      ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE,)


class CustomerEligibility(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.__store_algo360_data()
        self.customer_credit_limit = credit_service.CustomerCreditLimit(
            self.customer_id).limit
        self.loan_emi = None
        self.loan_tenure = None
        self.loan_amount = None
        self.__get_loan_product_data()

    def __store_algo360_data(self):
        algo360_data = {}
        login_objects = Login.objects.filter(customer_id=self.customer_id)
        if login_objects:
            imei = '864238035122424'
            # login_objects[0].imei
            customer_data = {
                'imei': imei,
                'customer_id': self.customer_id,
            }
            algo360 = algo360_service.Algo360(imei)
            # algo360 = algo360_service.Algo360(self.validated_data.get('customer_id'))
            algo360_data.update(algo360.get_model_data())
            algo360_objects = models.Algo360.objects.filter(
                customer_id=self.customer_id)
            if algo360_objects:
                models.Algo360.objects.filter(
                    customer_id=self.customer_id).update(**algo360_data)
                algo360_data.update(customer_data)
            else:
                algo360_data.update(customer_data)
                models.Algo360.objects.create(**algo360_data)

    def __get_loan_product_data(self):
        loan_product_objects = LoanProduct.objects.filter(
            customer_id=self.customer_id)
        if loan_product_objects:
            self.loan_emi = loan_product_objects[0].loan_emi
            self.loan_tenure = loan_product_objects[0].loan_tenure
            self.loan_amount = loan_product_objects[0].loan_amount

    def __get_tuned_loan_constants(self):
        loan_calculator = LoanCalculator(
            self.loan_amount, LOAN_CONSTANTS.get('rate_of_interest', .03))
        tuned_tenure = loan_calculator.loan_tenure_ceiled(
            self.customer_credit_limit)
        tuned_emi = loan_calculator.loan_emi_ceiled(tuned_tenure)
        customer_loan_constants = {
            'emi': tuned_emi,
            'tenure': tuned_tenure,
            'amount': self.loan_amount,
        }
        return customer_loan_constants

    def determine_eligibility(self):
        eligibility_data = {
            'customer_present_state': ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE,
            'tune_loan_product': False,
            'customer_loan_constants': {
                'emi': self.loan_emi,
                'tenure': self.loan_tenure,
                'amount': self.loan_amount,
            }
        }
        if self.customer_credit_limit >= self.loan_emi:
            register_customer_state(
                ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE, self.customer_id)
            eligibility_data[
                'customer_present_state'] = ELIGIBILITY_APPROVED_KYC_PROCCESSING_STATE
        else:
            register_customer_state(
                ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE, self.customer_id)
            eligibility_data[
                'customer_present_state'] = ELIGIBILITY_REJECTED_KYC_SUBMIT_STATE
            eligibility_data[
                'customer_loan_constants'] = self.__get_tuned_loan_constants()
            eligibility_data['tune_loan_product'] = True if eligibility_data['customer_loan_constants'][
                'tenure'] <= LOAN_CONSTANTS.get('loan_tenure_maximum') else False
        return eligibility_data
