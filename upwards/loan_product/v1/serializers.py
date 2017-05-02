from rest_framework import serializers
from decimal import Decimal

from django.conf import settings
from loan_product import models

from common.v1.utils.model_utils import check_pk_existence
from common.v1.exceptions import NotAcceptableError
from customer.models import Customer
from common.models import LoanPurpose
from services import loan_specifications_service, loan_agreement_service, loan_disbursal_service, loan_installment_service


class LoanProductSerializer(serializers.ModelSerializer):
    customer_id = serializers.IntegerField()
    loan_purpose_id = serializers.IntegerField()
    loan_interest_rate = Decimal(str(settings.LOAN_INTEREST_RATE))

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

    class Meta:
        model = models.LoanProduct
        exclude = ('customer', 'loan_purpose',
                   'created_at', 'updated_at', 'is_active')


class BikeLoanSerializer(serializers.ModelSerializer):
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
        model = models.BikeLoan
        exclude = ('customer', 'created_at', 'updated_at', 'is_active')


class LoanAgreementSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        valid_data = False
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if check_pk_existence(model_pk['model'], model_pk['pk']):
                    valid_data = True
        return valid_data

    def get_loan_data(self):
        return loan_agreement_service.LoanAgreement(self.validated_data.get('customer_id')).data


class LoanSpecificationsSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        valid_data = False
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if check_pk_existence(model_pk['model'], model_pk['pk']):
                    valid_data = True
        return valid_data

    def get_loan_specifications(self):
        loan_specifications = None
        customer_id = self.validated_data.get('customer_id')
        loan_id = None
        loan_product_id = None
        loan_product_objects = models.LoanProduct.objects.filter(
            customer_id=customer_id)
        if loan_product_objects:
            loan_product_index = len(loan_product_objects) - 1
            loan_product_id = loan_product_objects[loan_product_index].id
        loan_objects = models.Loan.objects.filter(customer_id=customer_id)
        if loan_objects:
            loan_index = len(loan_objects) - 1
            loan_id = loan_objects[loan_index].id
        if customer_id and loan_id and loan_product_id:
            loan_specifications = loan_specifications_service.LoanSpecifications(
                customer_id, loan_id, loan_product_id).data
        return loan_specifications


class LoanDisbursalSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        valid_data = False
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if check_pk_existence(model_pk['model'], model_pk['pk']):
                    valid_data = True
        return valid_data

    def get_loan_disbursal_details(self):
        loan_disbursal_details = None
        customer_id = self.validated_data.get('customer_id')
        loan_id = None
        loan_product_id = None
        loan_product_objects = models.LoanProduct.objects.filter(
            customer_id=customer_id)
        if loan_product_objects:
            loan_product_index = len(loan_product_objects) - 1
            loan_product_id = loan_product_objects[loan_product_index].id
        loan_objects = models.Loan.objects.filter(customer_id=customer_id)
        if loan_objects:
            loan_index = len(loan_objects) - 1
            loan_id = loan_objects[loan_index].id
        if customer_id and loan_id and loan_product_id:
            loan_disbursal_details = loan_disbursal_service.LoanDisbursal(
                customer_id, loan_id, loan_product_id).details()
        return loan_disbursal_details


class RepaymentDetailsSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        valid_data = False
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if check_pk_existence(model_pk['model'], model_pk['pk']):
                    valid_data = True
        return valid_data

    def get_repayment_details(self):
        repayment_details = None
        customer_id = self.validated_data.get('customer_id')
        loan_id = None
        loan_product_id = None
        loan_product_objects = models.LoanProduct.objects.filter(
            customer_id=customer_id)
        if loan_product_objects:
            loan_product_index = len(loan_product_objects) - 1
            loan_product_id = loan_product_objects[loan_product_index].id
        loan_objects = models.Loan.objects.filter(customer_id=customer_id)
        if loan_objects:
            loan_index = len(loan_objects) - 1
            loan_id = loan_objects[loan_index].id
        if customer_id and loan_id and loan_product_id:
            repayment_details = loan_installment_service.LoanInstallment(
                customer_id, loan_id, loan_product_id).get_repayment_data()
        return repayment_details


class CustomerLoanLoanProductSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()

    def validate_foreign_keys(self, data=None):
        valid_data = False
        data = data if data else self.validated_data
        model_pk_list = [
            {"model": Customer, "pk": data.get(
                'customer_id', -1), "pk_name": "customer_id"},
        ]
        for model_pk in model_pk_list:
            if model_pk["pk_name"] in data.keys():
                if check_pk_existence(model_pk['model'], model_pk['pk']):
                    valid_data = True
        return valid_data

    def get_loan_id(self):
        loan_id = None
        loan_objects = models.Loan.objects.filter(
            customer_id=self.validated_data.get('customer_id', -1))
        if loan_objects:
            loan_index = len(loan_objects) - 1
            loan_id = loan_objects[loan_index].id
        return loan_id

    def get_loan_product_id(self):
        loan_product_id = None
        loan_product_objects = models.LoanProduct.objects.filter(
            customer_id=self.validated_data.get('customer_id', -1))
        if loan_product_objects:
            loan_product_index = len(loan_product_objects) - 1
            loan_product_id = loan_product_objects[loan_product_index].id
        return loan_product_id


class RepaymentScheduleSerializer(CustomerLoanLoanProductSerializer):

    def get_repayment_schedule(self):
        repayment_schedule = None
        customer_id = self.validated_data.get('customer_id')
        loan_id = self.get_loan_id()
        loan_product_id = self.get_loan_product_id()
        if customer_id and loan_id and loan_product_id:
            repayment_schedule = loan_installment_service.LoanInstallment(
                customer_id, loan_id, loan_product_id).get_loan_installment_data()
        return repayment_schedule
