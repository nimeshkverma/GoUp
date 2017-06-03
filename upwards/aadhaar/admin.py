from django.contrib import admin
from aadhaar.models import Aadhaar


class AadhaarAdmin(admin.ModelAdmin):
    list_display = ("customer", "aadhaar", "aadhaar_source", "is_verified", "first_name",
                    "first_name_source", "last_name", "last_name_source", "father_first_name",
                    "father_first_name_source", "father_last_name", "father_last_name_source",
                    "mother_first_name", "mother_first_name_source", "mother_last_name", "mother_last_name_source",
                    "dob", "dob_source", "gender", "gender_source", "mobile_no", "mobile_no_source", "permanent_address_line1",
                    "permanent_address_line1_source", "permanent_address_line2", "permanent_address_line2_source",
                    "permanent_city", "permanent_city_source", "permanent_state", "permanent_state_source",
                    "permanent_pincode", "permanent_pincode_source", "pic_link", "pic_link_source",
                    "created_at", "updated_at", "is_active",)
    list_filter = ("aadhaar_source", "gender",)
    search_fields = ("customer__customer_id", "aadhaar", "first_name",
                     "last_name", "created_at", "updated_at", )

admin.site.register(Aadhaar, AadhaarAdmin)
