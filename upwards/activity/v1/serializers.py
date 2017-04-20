from rest_framework import serializers

from activity import models

from common.v1.utils.model_utils import check_pk_existence
from common.v1.exceptions import NotAcceptableError
from customer.models import Customer
from eligibility.v1.services.pre_loan_proccesing_service import CustomerPreLoanProccesing
from activity.models import register_customer_state


class CustomerStateSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if not check_pk_existence(model_pk['model'], model_pk['pk']):
                    raise NotAcceptableError(
                        model_pk['pk_name'], model_pk['pk'])

    class Meta:
        model = models.CustomerState
        exclude = ('customer', 'created_at', 'updated_at', 'is_active')


class KYCReviewSubmitSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def kyc_review_submission(self):
        pre_loan_proccesing_object = CustomerPreLoanProccesing(
            self.validated_data.get('customer_id'))
        register_customer_state(
            pre_loan_proccesing_object.customer_state, pre_loan_proccesing_object.customer_id)
        return {'customer_state': pre_loan_proccesing_object.customer_state}
