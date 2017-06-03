from django.contrib import admin
from transaction.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("customer", "loan", "amount", "utr", "transaction_status",
                    "transaction_type", "status_actor", "created_at", "updated_at",)
    list_filter = ("transaction_type",)
    search_fields = ("customer__customer_id", "loan", "amount", "utr", "transaction_status",
                     "transaction_type", "status_actor", "created_at", "updated_at",)

admin.site.register(Transaction, TransactionAdmin)
