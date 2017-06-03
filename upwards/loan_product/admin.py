from django.contrib import admin
from loan_product.models import LoanProduct, BikeLoan, Loan, Installment


class LoanProductAdmin(admin.ModelAdmin):
    list_display = ("customer", "loan_purpose", "loan_amount", "monthly_income", "existing_emi",
                    "loan_tenure", "loan_emi", "created_at", "updated_at",)
    list_filter = ("loan_purpose",)
    search_fields = ("customer__customer_id", "loan_purpose", "loan_amount", "monthly_income", "existing_emi",
                     "loan_tenure", "loan_emi", "created_at", "updated_at", )

admin.site.register(LoanProduct, LoanProductAdmin)


class BikeLoanAdmin(admin.ModelAdmin):
    list_display = ("customer", "brand", "model",
                    "manufacturing_year", "approximate_price", "down_payment", "created_at", "updated_at",)
    list_filter = ("brand",)
    search_fields = ("customer__customer_id", "brand", "model", "manufacturing_year",
                     "approximate_price", "down_payment", "created_at", "updated_at", )

admin.site.register(BikeLoan, BikeLoanAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("customer", "lender", "loan_amount_applied", "processing_fee", "tenure",
                    "interest_rate_per_tenure", "penalty_rate_per_tenure", "status", "application_datetime",
                    "disbursal_datetime", "security", "margin", "is_interest_deducted_at_source", "created_at", "updated_at",)
    list_filter = ("status",)
    search_fields = ("customer__customer_id", "lender", "loan_amount_applied", "processing_fee", "tenure",
                     "interest_rate_per_tenure", "penalty_rate_per_tenure", "status", "application_datetime",
                     "disbursal_datetime", "security", "margin", "is_interest_deducted_at_source", "created_at", "updated_at", )

admin.site.register(Loan, LoanAdmin)


class InstallmentAdmin(admin.ModelAdmin):
    list_display = ("loan", "installment_number", "expected_installment_amount", "expected_repayment_date",
                    "actual_installment_amount", "actual_repayment_date", "penalty_amount", "installment_paid",
                    "installment_interest_part", "installment_principal_part", "created_at", "updated_at",)
    search_fields = ("loan__customer", "installment_number", "expected_installment_amount", "expected_repayment_date",
                     "actual_installment_amount", "actual_repayment_date", "penalty_amount", "installment_paid",
                     "installment_interest_part", "installment_principal_part", "created_at", "updated_at",)

admin.site.register(Installment, InstallmentAdmin)
