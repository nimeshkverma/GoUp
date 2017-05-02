from activity.model_constants import LOAN_APPLICATION_PROCCESSED_STATE, LOAN_APPLICATION_ERRORED_STATE
from loan_product.models import Installment
from transaction.models import Transaction, INITIATED, UPWARDS, LOAN_AVAIL, COMPLETED
from loan_product.v1.services.loan_specifications_service import LoanSpecifications, Loan


class LoanDisbursal(object):

    def __init__(self, customer_id, loan_id, loan_product_id, loan_start_date=None, customer_state=None):
        self.customer_id = customer_id
        self.customer_state = customer_state
        self.loan_specifications = LoanSpecifications(
            self.customer_id, loan_id, loan_product_id, loan_start_date)

    def __create_installments(self):
        installments = []
        for installment_data in self.loan_specifications.repayment_profile:
            installments.append(Installment(
                loan_id=self.loan_specifications.loan_id,
                installment_number=installment_data['serial_no'],
                expected_installment_amount=installment_data['emi'],
                expected_repayment_date=installment_data['due_date'],
                installment_interest_part=installment_data['interest_paid'],
                installment_principal_part=installment_data['principal_paid']
            ))
        Installment.objects.bulk_create(installments)

    def __create_transaction(self):
        data = {
            'customer_id': self.customer_id,
            'loan_id': self.loan_specifications.loan_id,
            'transaction_status': INITIATED,
            'status_actor': UPWARDS,
            'transaction_type': LOAN_AVAIL,
            'amount': self.loan_specifications.loan_amount,
        }
        Transaction.objects.create(**data)

    def loan_post_processing(self):
        if self.customer_state == LOAN_APPLICATION_PROCCESSED_STATE:
            self.__create_installments()
            self.__create_transaction()

    def details(self):
        data = {
            'loan_id': self.loan_specifications.loan_id,
            'loan_amount': self.loan_specifications.loan_amount,
            'processing_fees': self.loan_specifications.processing_fee,
            'amount_transferred': 'N.A',
            'transaction_id': 'N.A',
            'transfer_date': 'N.A'
        }
        transaction_objects = Transaction.objects.filter(
            customer_id=self.customer_id, transaction_type=LOAN_AVAIL)
        if transaction_objects:
            transaction_index = len(transaction_objects) - 1
            data['amount_transferred'] = int(transaction_objects[
                transaction_index].amount) - int(data['processing_fees'])
            data['transaction_id'] = transaction_objects[transaction_index].id
            data['transfer_date'] = transaction_objects[
                transaction_index].updated_at.strftime("%Y-%m-%d")
        return data
