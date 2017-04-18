import datetime
from django.conf import settings
from loan_product.models import LoanProduct
from common.v1.utils.finance_utils import LoanCalculator
from customer.v1.service.homepage_config import LOAN_CONSTANTS


class LoanSpecifications(object):

    def __init__(self, customer_id, loan_start_date=None):
        self.customer_id = customer_id
        self.interest_rate = settings.LOAN_INTEREST_RATE
        self.loan_emi = None
        self.loan_tenure = None
        self.loan_amount = None
        self.__get_loan_product_data()
        self.loan_start_date = loan_start_date if loan_start_date else datetime.date.today()
        self.loan_calulator = LoanCalculator(
            self.loan_amount, self.interest_rate, self.loan_tenure, self.loan_emi)
        self.data = self.__data()

    def __get_loan_product_data(self):
        loan_product_objects = LoanProduct.objects.filter(
            customer_id=self.customer_id)
        if loan_product_objects:
            self.loan_emi = loan_product_objects[0].loan_emi
            self.loan_tenure = loan_product_objects[0].loan_tenure
            self.loan_amount = loan_product_objects[0].loan_amount
            self.interest_rate = float(
                loan_product_objects[0].loan_interest_rate)

    def __data(self):
        return self.loan_calulator.loan_table(self.loan_start_date)
