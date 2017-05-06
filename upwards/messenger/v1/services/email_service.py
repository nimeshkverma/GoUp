from django.core import signing
from django.core.mail import EmailMultiAlternatives
from rest_framework.reverse import reverse
from django.template.loader import get_template

from django.conf import settings
from customer.models import Customer
from eligibility.models import Profession
from documents.models import Documents, DocumentType
from activity.models import CustomerState, register_customer_state
from activity.model_constants import (FINANCE_SUBMIT_EMAIL_VERIFIED_STATE,
                                      FINANCE_SUBMIT_EMAIL_UNVERIFIED_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_VERIFIED_STATE,
                                      DOCUMENT_SUBMIT_EMAIL_UNVERIFIED_STATE,
                                      LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE,
                                      AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE)


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


def send_loan_agreement_email(customer_id):
    customer_state_object = CustomerState.objects.get(customer_id=customer_id)
    email_id = Customer.objects.get(customer_id=customer_id).alternate_email_id
    document_type_id = None
    template = None
    context_data = {}
    if customer_state_object.present_state == LOAN_SUBMIT_AGGREMENT_UNSIGNED_STATE:
        document_type_id = DocumentType.objects.get(
            name='unsigned_loan_agreement').id
        document_object = Documents.objects.get(
            customer_id=customer_id, document_type_id=document_type_id)
        template = get_template(
            'messenger/v1/unsigned_loan_agreement_email.html')
        context_data = {'document_link': document_object.document_1.url.split('?')[
            0]}
    elif customer_state_object.present_state == AGGREMENT_SIGNED_LOAN_APPLICATION_PROCCESSING_STATE:
        document_type_id = DocumentType.objects.get(
            name='signed_loan_agreement').id
        document_object = Documents.objects.get(
            customer_id=customer_id, document_type_id=document_type_id)
        template = get_template(
            'messenger/v1/signed_loan_agreement_email.html')
        context_data = {'document_link': document_object.document_1.url.split('?')[
            0]}
    else:
        pass
    if email_id and template and context_data:
        html_part = template.render(context_data)
        msg = EmailMultiAlternatives('Loan Agreement, Upwards',
                                     None, 'upwardstech@gmail.com', [email_id])
        msg.attach_alternative(html_part, 'text/html')
        msg.send(True)
