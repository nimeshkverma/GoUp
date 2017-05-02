from rest_framework import serializers

from transaction import models
from common.v1.utils.model_utils import check_pk_existence
from common.v1.exceptions import NotAcceptableError
from customer.models import Customer
from services import transaction_service


class TransactionHistoryDetailsSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id",
             "model": LoanPurpose, "pk": data.get(
                'loan_purpose_id', -1), "pk_name": "loan_purpose_ids"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if not check_pk_existence(model_pk['model'], model_pk['pk']):
                    raise NotAcceptableError(
                        model_pk['pk_name'], model_pk['pk'])

    def get_transaction_history(self):
        return transaction_service.TransactionHistory(self.validated_data.get('customer_id')).data
