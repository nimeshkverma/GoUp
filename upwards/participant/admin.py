from django.contrib import admin
from participant.models import Borrower, Lender


class BorrowerAdmin(admin.ModelAdmin):
    list_display = ("customer", "max_current_loans_allowed", "credit_limit", "number_of_active_loans", "number_of_repaid_loans",
                    "total_current_debt", "eligible_for_loan", )
    search_fields = ("customer__customer_id", "max_current_loans_allowed", "credit_limit", "number_of_active_loans", "number_of_repaid_loans",
                     "total_current_debt", "eligible_for_loan", "created_at", "updated_at", )

admin.site.register(Borrower, BorrowerAdmin)


class LenderAdmin(admin.ModelAdmin):
    list_display = ("name", "lender_type", "allocation_limit")
    search_fields = ("name", "lender_type", "allocation_limit",
                     "created_at", "updated_at", )

admin.site.register(Lender, LenderAdmin)
