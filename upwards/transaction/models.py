from __future__ import unicode_literals

from django.db import models

from common.models import ActiveObjectManager, ActiveModel


INITIATED = 'Initiated'
PROCESSING = 'Processing'
COMPLETED = 'Completed'

TRANSACTION_STATUS_CHOICES = (
    (INITIATED, 'Initiated'),
    (PROCESSING, 'Processing'),
    (COMPLETED, 'Completed'),
)

LOAN_AVAIL = 'Loan Availed'
INSTALLMENT_PAY = 'EMI Paid'
PENALTY_PAY = 'Penalty Paid'
PAST_INSTALLMENT_AND_PENALTY_PAY = 'Past EMI and Penalty Paid'
CURRENT_INSTALLMENT_PAST_INSTALLMENT_AND_PENALTY_PAY = 'Current EMI, Past EMI and Penalty Paid'
PROCESSING_FEE_PAY = 'Processing Fees Paid'

TRANSACTION_TYPE_CHOICES = (
    (LOAN_AVAIL, 'Loan Availed'),
    (INSTALLMENT_PAY, 'EMI Paid'),
    (PENALTY_PAY, 'Penalty Paid'),
    (PAST_INSTALLMENT_AND_PENALTY_PAY, 'Past EMI and Penalty Paid'),
    (CURRENT_INSTALLMENT_PAST_INSTALLMENT_AND_PENALTY_PAY,
     'Current EMI, Past EMI and Penalty Paid'),
    (PROCESSING_FEE_PAY, 'Processing Fees Paid'),
)

NBFC = 'nbfc'
UPWARDS = 'upwards'

STATUS_ACTOR_CHOICES = (
    (NBFC, 'NBFC'),
    (UPWARDS, 'Upwards'),
)


class Transaction(ActiveModel):
    customer = models.ForeignKey(
        'participant.Borrower', to_field="customer", on_delete=models.CASCADE)
    loan = models.ForeignKey('loan_product.Loan', on_delete=models.CASCADE)
    amount = models.IntegerField()
    installment = models.ForeignKey(
        'loan_product.Installment', on_delete=models.CASCADE, null=True, blank=True)
    utr = models.CharField(max_length=50, null=True, blank=True)
    transaction_status = models.CharField(
        max_length=50, default=INITIATED, choices=TRANSACTION_STATUS_CHOICES)
    transaction_type = models.CharField(
        max_length=50, default=LOAN_AVAIL, choices=TRANSACTION_TYPE_CHOICES)
    status_actor = models.CharField(
        max_length=50, default=UPWARDS, choices=STATUS_ACTOR_CHOICES)
    objects = models.Manager()
    active_objects = ActiveObjectManager()

    class Meta(object):
        db_table = "transaction"

    def __unicode__(self):
        return "%s__%s__%s__%s" % (str(self.customer_id), str(self.loan_id), str(self.installment_id), str(self.utr))
