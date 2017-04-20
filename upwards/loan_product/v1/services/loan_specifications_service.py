import datetime
from django.conf import settings
from loan_product.models import LoanProduct, Loan
from common.v1.utils.finance_utils import LoanCalculator
from customer.v1.service.homepage_config import LOAN_CONSTANTS


class LoanSpecifications(object):

    def __init__(self, customer_id, loan_start_date=None):
        self.customer_id = customer_id
        self.interest_rate = None
        self.emi = None
        self.tenure = None
        self.loan_amount = None
        self.number_of_emi = None
        self.processing_fee = None
        self.__set_aatributes()
        self.loan_start_date = loan_start_date if loan_start_date else datetime.date.today()
        self.repayment_profile = LoanCalculator(
            self.loan_amount, self.interest_rate, self.tenure, self.emi).loan_table(self.loan_start_date)
        self.data = self.__data()

    def __set_aatributes(self):
        loan_product_objects = LoanProduct.objects.filter(
            customer_id=self.customer_id)
        if loan_product_objects:
            self.emi = loan_product_objects[0].loan_emi
            self.tenure = loan_product_objects[0].loan_tenure
            self.loan_amount = loan_product_objects[0].loan_amount
            self.number_of_emi = self.tenure
        loan_objects = Loan.objects.filter(customer_id=self.customer_id)
        if loan_objects:
            self.interest_rate = float(
                loan_objects[0].interest_rate_per_tenure)
            self.processing_fee = loan_objects[0].processing_fee

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
