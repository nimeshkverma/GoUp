import datetime
from common.v1.utils.finance_utils import PenaltyCalulator
from loan_product.models import Loan, LoanProduct, Installment


class LoanInstallment(object):

    def __init__(self, customer_id, loan_id, loan_product_id):
        self.customer_id = customer_id
        self.loan_id = loan_id
        self.loan_product_id = loan_product_id
        self.emi = None
        self.loan_object = self.__get_loan_object()
        self.loan_product_object = self.__get_loan_product_object()
        self.emi_data = self.__set_emi_data()
        self.loan_data = self.__set_loan_data()

    def __get_loan_object(self):
        return Loan.objects.get(pk=self.loan_id)

    def __get_loan_product_object(self):
        return LoanProduct.objects.get(pk=self.loan_product_id)

    def __installment_status(self, installment_object):
        if installment_object.installment_paid:
            return 'paid'
        if datetime.date.today() <= installment_object.expected_repayment_date.date():
            return 'unpaid_no_penalty'
        else:
            return 'unpaid_with_penalty'

    def __penalty(self, installment_object):
        return PenaltyCalulator(installment_object.expected_installment_amount, self.loan_object.interest_rate_per_tenure,
                                self.loan_object.penalty_rate_per_tenure, installment_object.expected_repayment_date.date()).penalty

    def __set_emi_data(self):
        emi_data = []
        loan_principal = self.loan_object.loan_amount_applied
        installment_objects = Installment.objects.filter(
            loan_id=self.loan_id).order_by('installment_number')
        for installment_object in installment_objects:
            installment_status = self.__installment_status(installment_object)
            installment_data = {
                'serial_no': installment_object.installment_number,
                'due_date': installment_object.expected_repayment_date.strftime("%Y-%m-%d"),
                'emi': installment_object.expected_installment_amount,
                'principal_paid': installment_object.installment_principal_part,
                'interest_paid': installment_object.installment_interest_part,
                'month': installment_object.expected_repayment_date.strftime("%b"),
                'installment_status': installment_status,
                'principal_outstanding': loan_principal - installment_object.installment_principal_part if installment_status != 'unpaid_with_penalty' else loan_principal,
                'penalty': self.__penalty(installment_object)
            }
            emi_data.append(installment_data)
        self.emi = installment_object.expected_installment_amount
        return emi_data

    def __set_loan_data(self):
        loan_data = {
            "loan_amount": self.loan_object.loan_amount_applied,
            "loan_interest": self.loan_object.interest_rate_per_tenure,
            "emi": self.emi,
            "processing_fee": self.loan_object.processing_fee,
            "tenure": self.loan_object.tenure,
        }
        return loan_data

    def get_loan_installment_data(self):
        graph_data = {
            'loan_details': self.loan_data,
            'emi_details': self.emi_data,
        }
        return graph_data

    def get_repayment_data(self):
        next_emi_amount = 0
        next_emi_due_date = None
        past_emi_due = 0
        late_payment_penalty = 0
        installment_objects = Installment.objects.filter(
            loan_id=self.loan_id).order_by('installment_number')
        for installment_object in installment_objects:
            past_emi_due = past_emi_due + installment_object.expected_installment_amount if self.__installment_status(
                installment_object) == 'unpaid_with_penalty' else past_emi_due
            late_payment_penalty += self.__penalty(installment_object)
            next_emi_amount = installment_object.expected_installment_amount
            next_emi_due_date = installment_object.expected_repayment_date.strftime(
                "%Y-%m-%d")
            if datetime.date.today() <= installment_object.expected_repayment_date.date():
                break
        repayment_data = {
            "next_emi_amount": next_emi_amount,
            "next_emi_due_date": next_emi_due_date,
            "past_emi_due": past_emi_due,
            "late_payment_penalty": late_payment_penalty,
            "total_past_payment_due": past_emi_due + late_payment_penalty,
            "total_past_and_next_payment_due": past_emi_due + late_payment_penalty + next_emi_amount,
        }
        return repayment_data
