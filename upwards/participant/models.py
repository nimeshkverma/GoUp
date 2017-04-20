from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save

from common.models import InActiveModel, ActiveObjectManager, ActiveModel
from activity.models import register_customer_state
from activity.model_constants import ELIGIBILITY_SUBMIT_STATE

NBFC = 'nbfc'
BANK = 'bank'
LENDER_TYPE_CHOICES = (
    (NBFC, 'NBFC'),
    (BANK, 'Bank'),
)


class Borrower(InActiveModel):
    customer = models.OneToOneField(
        'customer.Customer', on_delete=models.CASCADE)
    max_current_loans_allowed = models.IntegerField(default=1)
    credit_limit = models.IntegerField()
    number_of_active_loans = models.IntegerField(default=0)
    number_of_repaid_loans = models.IntegerField(default=0)
    total_current_debt = models.IntegerField(default=0)
    eligible_for_loan = models.BooleanField(
        default=True)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    @staticmethod
    def register_eligibility_result_approved_customer_state(sender, instance, created, **kwargs):
        if created:
            register_customer_state(
                ELIGIBILITY_SUBMIT_STATE, instance.customer_id)

    class Meta(object):
        db_table = "borrower"

    def __unicode__(self):
        return "%s__%s__%s" % (str(self.customer_id), str(self.credit_limit), str(self.total_current_debt))

post_save.connect(
    Borrower.register_eligibility_result_approved_customer_state, sender=Borrower)


class Lender(ActiveModel):
    name = models.CharField(max_length=100, unique=True)
    lender_type = models.CharField(
        max_length=50, default=NBFC, choices=LENDER_TYPE_CHOICES)
    allocation_limit = models.IntegerField(default=10000000)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = "lender"

    def __unicode__(self):
        return "%s__%s__%s" % (str(self.id), str(self.name), str(self.lender_type))
