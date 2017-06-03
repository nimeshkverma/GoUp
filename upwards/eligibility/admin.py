from django.contrib import admin
from eligibility.models import Finance, Profession, Education, Vahan


class FinanceAdmin(admin.ModelAdmin):
    list_display = ("customer", "any_active_loans", "any_owned_vehicles", "vehicle_type", "marital_status",
                    "dependents", "phone_no", "created_at", "updated_at", "is_active")
    list_filter = ("vehicle_type", "marital_status",)
    search_fields = ("customer__customer_id", "any_active_loans", "any_owned_vehicles", "vehicle_type",
                     "marital_status", "phone_no", "created_at", "updated_at", )

admin.site.register(Finance, FinanceAdmin)


class ProfessionAdmin(admin.ModelAdmin):
    list_display = ("customer", "company", "salary", "organisation_type", "salary_payment_mode", "phone_no",
                    "is_phone_no_verified", "profession_type", "email", "is_email_verified", "department", "designation", "office_city",)
    search_fields = ("customer__customer_id", "email",
                     "salary", "created_at", "updated_at", )

admin.site.register(Profession, ProfessionAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ("customer", "college", "qualification",
                    "completion_year", "qualification_type",)
    search_fields = ("customer__customer_id", "qualification",
                     "created_at", "updated_at", )

admin.site.register(Education, EducationAdmin)


class VahanAdmin(admin.ModelAdmin):
    list_display = ("customer", "registration_no", "make", "model", "make_model", "fuel", "display_variant", "short_variant",
                    "vehicle_id", "vertical", "rto_code", "rto_lnt_location", "rto_plate_lnt_location", "registration_date")
    search_fields = ("customer__customer_id", "registration_no",
                     "created_at", "updated_at", )

admin.site.register(Vahan, VahanAdmin)
