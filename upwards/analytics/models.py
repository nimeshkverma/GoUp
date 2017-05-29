from __future__ import unicode_literals

from decimal import Decimal
from django.db import models

from django.db.models.signals import post_save
from activity.models import register_customer_state
from activity.model_constants import PAN_SUBMIT_STATE, CUSTOMER, PAN_SUBMIT

from common.models import (ActiveModel,
                           ActiveObjectManager,
                           numeric_regex,)


class Algo360(ActiveModel):
    customer = models.OneToOneField(
        'customer.Customer', on_delete=models.CASCADE)
    imei = models.CharField(
        validators=[numeric_regex], editable=False, blank=True, null=False, max_length=16)
    monthly_average_balance_lifetime = models.CharField(
        max_length=100, blank=True, null=False)
    monthly_average_balance_12 = models.CharField(
        max_length=100, blank=True, null=False)
    monthly_average_balance_6 = models.CharField(
        max_length=100, blank=True, null=False)
    monthly_average_balance_3 = models.CharField(
        max_length=100, blank=True, null=False)
    monthly_average_balance_1 = models.CharField(
        max_length=100, blank=True, null=False)
    number_of_cheque_bounce_1 = models.CharField(
        max_length=100, blank=True, null=False)
    number_of_cheque_bounce_3 = models.CharField(
        max_length=100, blank=True, null=False)
    is_credit_card_overlimited = models.CharField(max_length=100, default=True)
    credit_card_last_payment_due = models.CharField(
        max_length=100, blank=True, null=False)
    salary = models.CharField(max_length=100, blank=True, null=False)
    algo360_data = models.TextField(editable=False, blank=True, null=False)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = "analytics_algo360"

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.monthly_average_balance_lifetime), str(self.salary))

CALL = 'Call'
SMS = 'SMS'
DATA_USAGE = 'Data Usage'

LOG_TYPE_CHOICES = (
    (CALL, 'Call'),
    (SMS, 'SMS'),
    (DATA_USAGE, 'Data Usage'),
)


class DataLog(ActiveModel):
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE)
    log_type = models.CharField(
        max_length=50, default=SMS, choices=LOG_TYPE_CHOICES)
    log_data = models.TextField(blank=False, null=False)

    class Meta(object):
        db_table = "data_log"

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.log_type), str(self.created_at))


DEVICE_DATA_CALL = 'Call'
DEVICE_DATA_SMS = 'SMS'
DEVICE_DATA_INTERNET = 'Internet'

DEVICE_DATA_TYPE_CHOICES = (
    (DEVICE_DATA_CALL, 'Call'),
    (DEVICE_DATA_SMS, 'SMS'),
    (DEVICE_DATA_INTERNET, 'Internet'),
)

INCOMING = 'Incoming'
OUTGOING = 'Outgoing'
OUTGOING_INCOMING = 'Outgoing/Incoming'
MISSED = 'Missed'

STATUS_CHOICES = (
    (INCOMING, 'Incoming'),
    (OUTGOING, 'Outgoing'),
    (MISSED, 'Missed'),
    (OUTGOING_INCOMING, 'Outgoing/Incoming'),
)

COUNT = 'Count'
DURATION = 'Duration'
COUNT_RATIO = 'Count Ratio'
DURATION_RATIO = 'Duration Ratio'

ATTRIBUTE_CHOICES = (
    (COUNT, 'Count'),
    (DURATION, 'Duration'),
    (COUNT_RATIO, 'Count Ratio'),
    (DURATION_RATIO, 'Duration Ratio'),
)

WEEKDAY = 'Weekday'
WEEKEND = 'Weekend'
WEEK = 'Week'

WEEKDAY_CHOICES = (
    (WEEKDAY, 'Weekday'),
    (WEEKEND, 'Weekend'),
    (WEEK, 'Week'),
)

MORNING = 'Morning'
OFFICE_HOURS = 'Office Hours'
EVENING = 'Evening'
LATE_NIGHT = 'Late Night'
ALL = 'All'

DAY_HOUR_TYPE_CHOICES = (
    (MORNING, 'Morning'),
    (OFFICE_HOURS, 'Office Hours'),
    (EVENING, 'Evening'),
    (LATE_NIGHT, 'Late Night'),
    (ALL, 'All'),
)


class DeviceData(ActiveModel):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    data_type = models.CharField(
        max_length=50, default=DEVICE_DATA_CALL, choices=DEVICE_DATA_TYPE_CHOICES)
    status = models.CharField(
        max_length=50, blank=True, null=True, default=INCOMING, choices=STATUS_CHOICES)
    attribute = models.CharField(
        max_length=50, default=COUNT, choices=ATTRIBUTE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=4)
    weekday_type = models.CharField(
        max_length=50, default=WEEKDAY, choices=WEEKDAY_CHOICES)
    day_hour_type = models.CharField(
        max_length=50, default=ALL, choices=DAY_HOUR_TYPE_CHOICES)

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.data_type), str(self.status))


CONTACT_DATA_NO_OF_CONTACTS = 'Number of Contacts'

CONTACT_DATA_TYPE_CHOICES = (
    (CONTACT_DATA_NO_OF_CONTACTS, 'Number of Contacts'),
)


class ContactData(ActiveModel):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    data_type = models.CharField(
        max_length=50, default=CONTACT_DATA_NO_OF_CONTACTS, choices=CONTACT_DATA_TYPE_CHOICES)
    value = models.DecimalField(max_digits=10, decimal_places=4)

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.data_type), str(self.status))


SIGNUP = 'signup'
LOAN_PRODUCT = 'loan product'
PAN = 'pan'
PROFESSION = 'profession'
EDUCATION = 'education'
FINANCEAADHAAR = 'financeaadhaar'
AADHAAR_DETAILS = 'aadhaar details'
BANK = 'bank'
PERSONAL_CONTACT = 'personal contact'
DOCUMENTS = 'documents'
ELIGIBILITY_REVIEW = 'eligibility review'
KYC_REVIEW = 'kyc_review'

SCREEN_CHOICES = (
    (SIGNUP, 'signup'),
    (LOAN_PRODUCT, 'loan product'),
    (PAN, 'pan'),
    (PROFESSION, 'profession'),
    (EDUCATION, 'education'),
    (FINANCEAADHAAR, 'financeaadhaar'),
    (AADHAAR_DETAILS, 'aadhaar details'),
    (BANK, 'bank'),
    (PERSONAL_CONTACT, 'personal contact'),
    (DOCUMENTS, 'documents'),
    (ELIGIBILITY_REVIEW, 'eligibility review'),
    (KYC_REVIEW, 'kyc_review'),
)

CREATE = 'create'
UPDATE = 'update'

MODE_CHOICES = (
    (CREATE, 'create'),
    (UPDATE, 'update'),
)


class ScreenEventData(ActiveModel):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    time_spent = models.IntegerField(null=False, blank=False, default=0)
    sessions = models.IntegerField(null=False, blank=False, default=1)
    screen = models.CharField(
        max_length=50, default=SIGNUP, choices=SCREEN_CHOICES)
    mode = models.CharField(
        max_length=50, default=CREATE, choices=MODE_CHOICES)

    class Meta(object):
        db_table = "analytics_screen_eventdata"

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.screen), str(self.time_spent))


class FieldEventData(ActiveModel):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    screen = models.CharField(
        max_length=50, default=SIGNUP, choices=SCREEN_CHOICES)
    field = models.CharField(max_length=100, default="")
    edits = models.IntegerField(null=False, blank=False, default=1)
    deviation = models.DecimalField(max_digits=10, decimal_places=4)
    mode = models.CharField(
        max_length=50, default=CREATE, choices=MODE_CHOICES)

    class Meta(object):
        db_table = "analytics_field_eventdata"

    def __unicode__(self):
        return '%s__%s__%s' % (str(self.customer), str(self.screen), str(self.field))
