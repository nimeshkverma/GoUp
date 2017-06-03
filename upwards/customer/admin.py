from django.contrib import admin
from customer.models import Customer, BankDetails


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "alternate_email_id", "is_alternate_email_id_verified", "alternate_mob_no", "is_alternate_mob_no_verified",
                    "current_address_line1", "current_address_line2", "current_city", "current_state", "current_pincode", "created_at", "updated_at", "is_active")
    search_fields = ("customer_id", "alternate_email_id", "alternate_mob_no")

admin.site.register(Customer, CustomerAdmin)


class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ("customer", "bank_name", "account_number", "account_holder_name", "branch_detail",
                    "ifsc", "upi_mobile_number", "is_upi_mobile_number_verified", "created_at", "updated_at", "is_active")
    search_fields = ("customer__customer_id", "bank_name",
                     "account_number", "account_holder_name")

admin.site.register(BankDetails, BankDetailsAdmin)
