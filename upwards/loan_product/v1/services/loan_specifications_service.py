import datetime
from django.conf import settings
from loan_product.models import LoanProduct, Loan
from common.v1.utils.finance_utils import LoanCalculator
from customer.v1.service.homepage_config import LOAN_CONSTANTS


class LoanSpecifications(object):

    def __init__(self, customer_id, loan_id, loan_product_id, loan_start_date=None):
        self.customer_id = customer_id
        self.loan_id = loan_id
        self.loan_product_id = loan_product_id
        self.interest_rate = None
        self.emi = None
        self.tenure = None
        self.loan_amount = None
        self.number_of_emi = None
        self.processing_fee = None
        self.__set_attributes()
        self.loan_start_date = loan_start_date if loan_start_date else datetime.date.today()
        self.repayment_profile = LoanCalculator(
            self.loan_amount, self.interest_rate, self.tenure, self.emi).loan_table(self.loan_start_date)
        self.data = self.__data()

    def __set_attributes(self):
        loan_product_object = LoanProduct.objects.get(pk=self.loan_product_id)
        self.emi = loan_product_object.loan_emi
        self.tenure = loan_product_object.loan_tenure
        self.loan_amount = loan_product_object.loan_amount
        self.number_of_emi = self.tenure
        loan_object = Loan.objects.get(pk=self.loan_id)
        self.interest_rate = float(loan_object.interest_rate_per_tenure)
        self.processing_fee = loan_object.processing_fee

    def __data(self):
        data = {
            'customer_id': self.customer_id,
            'loan_amount': self.loan_amount,
            'tenure': self.tenure,
            'emi': self.emi,
            'number_of_emi': self.number_of_emi,
            'loan_interest': self.interest_rate,
            'processing_fee': self.processing_fee,
            'repayment_profile': self.repayment_profile,
        }
        return data
