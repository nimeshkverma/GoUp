from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from common.models import ActiveObjectManager, ActiveModel
from activity.models import register_customer_state
from activity.model_constants import LOAN_PRODUCT_SUBMIT_STATE


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
