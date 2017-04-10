from rest_framework import serializers

from messenger import models

from common.v1.utils.model_utils import check_pk_existence
from common.v1.exceptions import NotAcceptableError
from customer.models import Customer
from services import notification_service


class EmailVerificationSerializer(serializers.ModelSerializer):
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

    def save(self):
        data = self.validated_data
        email_verification_objects = models.EmailVerification.objects.filter(
            customer_id=data['customer_id'], email_id=data['email_id'], email_type=data['email_type'])
        if email_verification_objects:
            email_verification_object = email_verification_objects[0]
        else:
            email_verification_object = models.EmailVerification.objects.create(
                **data)
        return email_verification_object

    class Meta:
        model = models.EmailVerification
        exclude = ('customer', 'created_at',
                   'updated_at', 'is_active', 'id', 'times')


class OtpSerializer(serializers.ModelSerializer):
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
        model = models.Otp
        exclude = ('customer', 'created_at', 'updated_at',
                   'is_active', 'id', 'times', 'is_verified')


class PreSignupDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PreSignupData
        exclude = ('created_at', 'updated_at', 'is_active',)


class NotificationSerializer(serializers.ModelSerializer):

    def send_notification(self):
        message_title = self.validated_data.get('message_title')
        message_body = self.validated_data.get('message_body')
        notification_type = self.validated_data.get('notification_type')
        notification = notification_service.Notification(
            message_title, message_body, notification_type)
        notification.send_notifications()

    class Meta:
        model = models.Notification
        exclude = ('created_at', 'updated_at', 'is_active',)
