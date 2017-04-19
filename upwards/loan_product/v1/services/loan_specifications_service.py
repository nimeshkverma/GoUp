import datetime
from django.conf import settings
from loan_product.models import LoanProduct
from common.v1.utils.finance_utils import LoanCalculator
from customer.v1.service.homepage_config import LOAN_CONSTANTS


class LoanSpecifications(object):

    def __init__(self, customer_id, loan_start_date=None):
        self.customer_id = customer_id
    #     self.interest_rate = settings.LOAN_INTEREST_RATE
    #     self.loan_emi = None
    #     self.loan_tenure = None
    #     self.loan_amount = None
    #     self.__get_loan_product_data()
    #     self.loan_start_date = loan_start_date if loan_start_date else datetime.date.today()
    #     self.loan_calulator = LoanCalculator(
    # self.loan_amount, self.interest_rate, self.loan_tenure, self.loan_emi)
        self.data = self.__data()

    # def __get_loan_product_data(self):
    #     loan_product_objects = LoanProduct.objects.filter(
    #         customer_id=self.customer_id)
    #     if loan_product_objects:
    #         self.loan_emi = loan_product_objects[0].loan_emi
    #         self.loan_tenure = loan_product_objects[0].loan_tenure
    #         self.loan_amount = loan_product_objects[0].loan_amount
    #         self.interest_rate = float(
    #             loan_product_objects[0].loan_interest_rate)

    def __data(self):
        # return self.loan_calulator.loan_table(self.loan_start_date)
        dummy = {
            'loan_amount': 10000,
            'tenure': 5,
            'emi': 2184,
            'number_of_emi': 5,
            'loan_interest': 0.03,
            'processing_fee': 1000,
            'repayment_profile': [{'due_date': '2017-05-17',
                                   'serial_no': 1,
                                   'emi': 2184,
                                   'interest_paid': 300,
                                   'principal_outstanding': 10000,
                                   'principal_paid': 1884},
                                  {'due_date': '2017-06-17',
                                   'serial_no': 2,
                                   'emi': 2184,
                                   'interest_paid': 244,
                                   'principal_outstanding': 8117,
                                   'principal_paid': 1941},
                                  {'due_date': '2017-07-17',
                                   'serial_no': 3,
                                   'emi': 2184,
                                   'interest_paid': 186,
                                   'principal_outstanding': 6177,
                                   'principal_paid': 1999},
                                  {'due_date': '2017-08-17',
                                   'serial_no': 4,
                                   'emi': 2184,
                                   'interest_paid': 126,
                                   'principal_outstanding': 4179,
                                   'principal_paid': 2059},
                                  {'due_date': '2017-09-17',
                                   'serial_no': 5,
                                   'emi': 2184,
                                   'interest_paid': 64,
                                   'principal_outstanding': 2120,
                                   'principal_paid': 2120}]
        }

        return dummy
