import datetime
from transaction.models import Transaction, COMPLETED


class TransactionHistory(object):

    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.data = self.__set_transaction_history_data()

    def __set_transaction_history_data(self):
        transaction_history = []
        transaction_objects = Transaction.objects.filter(
            customer_id=self.customer_id, transaction_status=COMPLETED).order_by('created_at')
        for transaction_object in transaction_objects:
            data = {
                'loan_id': transaction_object.loan.id,
                'installment_id': transaction_object.installment.id if transaction_object.installment else None,
                'amount': transaction_object.amount,
                'utr': transaction_object.utr,
                'transaction_status': transaction_object.transaction_status,
                'transaction_type': transaction_object.transaction_type,
                'status_actor': transaction_object.status_actor,
                'created_at': transaction_object.created_at.strftime("%Y-%m-%d"),
                'updated_at': transaction_object.updated_at.strftime("%Y-%m-%d"),
            }
            transaction_history.append(data)
        return {
            'transaction_history': transaction_history
        }
