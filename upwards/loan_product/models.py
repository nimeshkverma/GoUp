from __future__ import unicode_literals

from decimal import Decimal
from django.db import models
from django.db.models.signals import post_save
from common.models import ActiveObjectManager, ActiveModel
from activity.models import register_customer_state
from activity.model_constants import LOAN_PRODUCT_SUBMIT_STATE

PRE_PROCESS = 'pre_process'
PROCESSING = 'processing'
REJECTED = 'rejected'
DISBURSED = 'disbursed'
COMPLETLY_PAID = 'completly_paid'
PARTIALLY_PAID = 'partially_paid'
BANK = 'bank'
LOAN_STATUS_CHOICES = (
    (PRE_PROCESS, 'pre_process'),
    (PROCESSING, 'processing'),
    (REJECTED, 'rejected'),
    (DISBURSED, 'disbursed'),
    (COMPLETLY_PAID, 'completly_paid'),
    (PARTIALLY_PAID, 'partially_paid'),
)


class LoanProduct(ActiveModel):
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE)
    loan_purpose = models.ForeignKey(
        'common.LoanPurpose', on_delete=models.CASCADE)
    loan_amount = models.IntegerField(default=0, null=False, blank=False)
    monthly_income = models.IntegerField(default=0, null=False, blank=False)
    existing_emi = models.IntegerField(default=0, null=False, blank=False)
    loan_tenure = models.IntegerField(default=0, null=False, blank=False)
    loan_emi = models.IntegerField(default=0, null=False, blank=False)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    @staticmethod
    def register_product_submit_customer_state(sender, instance, created, **kwargs):
        if created:
            register_customer_state(
                LOAN_PRODUCT_SUBMIT_STATE, instance.customer_id)

    class Meta(object):
        unique_together = ('customer', 'id')
        db_table = 'loan_product'

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.customer_id), str(self.loan_purpose), str(self.loan_amount), str(self.loan_tenure))

post_save.connect(
    LoanProduct.register_product_submit_customer_state, sender=LoanProduct)


class BikeLoan(ActiveModel):
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE)
    brand = models.CharField(blank=False, null=False, max_length=256)
    model = models.CharField(blank=False, null=False, max_length=256)
    manufacturing_year = models.CharField(
        blank=False, null=False, max_length=256)
    approximate_price = models.IntegerField(blank=False, null=False)
    down_payment = models.IntegerField(blank=False, null=False)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = 'bike_loan'

    def __unicode__(self):
        return "%s__%s__%s__%s__%s" % (str(self.customer_id), str(self.brand), str(self.model), str(self.manufacturing_year), str(self.approximate_price))


class Loan(ActiveModel):
    customer = models.ForeignKey(
        'customer.Customer', on_delete=models.CASCADE)
    lender = models.ForeignKey('participant.Lender')
    loan_amount_applied = models.IntegerField(null=False, blank=False)
    processing_fee = models.IntegerField(null=False, blank=False)
    tenure = models.IntegerField(null=False, blank=False)
    interest_rate_per_tenure = models.DecimalField(
        max_digits=6, decimal_places=4)
    penalty_rate_per_tenure = models.DecimalField(
        max_digits=6, decimal_places=4)
    status = models.CharField(
        max_length=50, default=PRE_PROCESS, choices=LOAN_STATUS_CHOICES)
    application_datetime = models.DateTimeField(null=True, blank=True)
    disbursal_datetime = models.DateTimeField(null=True, blank=True)
    security = models.CharField(max_length=200, default='PDC')
    margin = models.IntegerField(null=True, blank=True, default=0)
    is_interest_deducted_at_source = models.BooleanField(default=False)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = "loan"

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.customer_id), str(self.status), str(self.loan_amount_applied), str(self.application_datetime))


class Installment(ActiveModel):
    loan = models.ForeignKey(
        'Loan', on_delete=models.CASCADE)
    installment_number = models.IntegerField()
    expected_installment_amount = models.IntegerField()
    expected_repayment_date = models.DateTimeField()
    actual_installment_amount = models.IntegerField(null=True, blank=True)
    actual_repayment_date = models.DateTimeField(null=True, blank=True)
    penalty_amount = models.IntegerField(null=True, blank=True)
    installment_paid = models.BooleanField(default=False)
    installment_interest_part = models.IntegerField()
    installment_principal_part = models.IntegerField()
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = "installment"

    def __unicode__(self):
        return "%s__%s" % (str(self.id), str(self.loan_id))
