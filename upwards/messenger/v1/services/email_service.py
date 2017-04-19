from django.core import signing
from django.core.mail import EmailMultiAlternatives
from rest_framework.reverse import reverse
from django.template.loader import get_template

from django.conf import settings
from customer.models import Customer
from eligibility.models import Profession
from activity.models import CustomerState, register_customer_state
from activity.model_constants import (FINANCE_SUBMIT_EMAIL_VERIFIED_STATE,
                                      FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE)


def send_verification_mail(email_verify_data):
    encoded_data = signing.dumps(email_verify_data)
    verification_link = settings.VERSIONED_BASE_URL[
        'v1'] + 'customer/verify_email/' + encoded_data
    template = get_template('messenger/v1/email_verify.html')
    html_part = template.render({'verification_link': verification_link})
    msg = EmailMultiAlternatives('Email verification Link, Upwards',
                                 None, 'upwardstech@gmail.com', [email_verify_data['email_id']])
    msg.attach_alternative(html_part, 'text/html')
    msg.send(True)


def update_email_models(email_object):
    def profession_email_verify_state(email_object):
        print Profession.objects.filter(customer_id=email_object.customer_id)
        Profession.objects.filter(customer_id=email_object.customer_id).update(
            **{'is_email_verified': email_object.is_verified})
        if CustomerState.objects.get(customer_id=email_object.customer_id).present_state == FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE:
            print "jj"
            register_customer_state(
                FINANCE_SUBMIT_EMAIL_VERIFIED_STATE, email_object.customer_id)

    def alternate_email_verify_state(email_object):
        Customer.objects.filter(customer_id=email_object.customer_id).update(
            **{'is_alternate_email_id_verified': email_object.is_verified})
        if CustomerState.objects.get(customer_id=email_object.customer_id).present_state == DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE:
            register_customer_state(
                DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE, email_object.customer_id)

    if email_object.email_type == 'customer_alternate_email':
        alternate_email_verify_state(email_object)
    if email_object.email_type == 'customer_profession_email':
        profession_email_verify_state(email_object)
