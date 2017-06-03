from django.contrib import admin
from common.models import College, Company, SalaryPaymentMode, OrganisationType, ProfessionType, LoanPurpose, Bike


class CollegeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    search_fields = ("name", )

admin.site.register(College, CollegeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    search_fields = ("name", )

admin.site.register(Company, CompanyAdmin)


class SalaryPaymentModeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    search_fields = ("name", )

admin.site.register(SalaryPaymentMode, SalaryPaymentModeAdmin)


class OrganisationTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    search_fields = ("name", )

admin.site.register(OrganisationType, OrganisationTypeAdmin)


class ProfessionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name", "created_at", "updated_at", "is_active")
    search_fields = ("type_name", )

admin.site.register(ProfessionType, ProfessionTypeAdmin)


class LoanPurposeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at", "is_active")
    search_fields = ("name", )

admin.site.register(LoanPurpose, LoanPurposeAdmin)


class BikeAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "model", "manufacturing_year", "approximate_price",
                    "down_payment", "created_at", "updated_at", "is_active")
    search_fields = ("brand", "model", "manufacturing_year",)
