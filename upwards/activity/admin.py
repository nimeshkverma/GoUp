from django.contrib import admin
from activity.models import CustomerState


class CustomerStateAdmin(admin.ModelAdmin):
    list_display = ("customer", "present_state", "from_state", "to_state",
                    "comments", "created_at", "updated_at", "is_active",)
    list_filter = ("present_state", "is_active",)
    search_fields = ("customer__customer_id", "present_state",
                     "from_state", "created_at", "updated_at", )

admin.site.register(CustomerState, CustomerStateAdmin)
