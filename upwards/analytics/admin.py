from django.contrib import admin
from analytics.models import Algo360, DataLog, DeviceData, ContactData, ScreenEventData, FieldEventData


class Algo360Admin(admin.ModelAdmin):
    list_display = ("customer", "imei", "monthly_average_balance_lifetime", "monthly_average_balance_12", "monthly_average_balance_6",
                    "monthly_average_balance_3", "monthly_average_balance_1", "number_of_cheque_bounce_1", "number_of_cheque_bounce_3",
                    "is_credit_card_overlimited", "credit_card_last_payment_due", "salary",
                    "created_at", "updated_at", "is_active")
    search_fields = ("customer__customer_id", "monthly_average_balance_lifetime",
                     "salary", "created_at", "updated_at", )

admin.site.register(Algo360, Algo360Admin)


class DeviceDataAdmin(admin.ModelAdmin):
    list_display = ("customer", "data_type", "status", "attribute", "value",
                    "weekday_type", "day_hour_type",
                    "created_at", "updated_at", "is_active")
    list_filter = ("data_type", "status", "attribute",
                   "value", "weekday_type", "day_hour_type")
    search_fields = ("customer__customer_id", "data_type", "status",
                     "attribute", "value", "weekday_type", "day_hour_type", )

admin.site.register(DeviceData, DeviceDataAdmin)


class ContactDataAdmin(admin.ModelAdmin):
    list_display = ("customer", "data_type", "value",
                    "created_at", "updated_at", "is_active")
    list_filter = ("data_type",)
    search_fields = ("customer__customer_id", "data_type", )

admin.site.register(ContactData, ContactDataAdmin)


class ScreenEventDataAdmin(admin.ModelAdmin):
    list_display = ("customer", "time_spent", "sessions", "screen", "mode",
                    "created_at", "updated_at", "is_active")
    list_filter = ("screen", "mode",)
    search_fields = ("customer__customer_id", "time_spent",
                     "sessions", "screen", "mode", )

admin.site.register(ScreenEventData, ScreenEventDataAdmin)


class FieldEventDataAdmin(admin.ModelAdmin):
    list_display = ("customer", "edits", "deviation", "screen", "mode", "field",
                    "created_at", "updated_at", "is_active",)
    list_filter = ("screen", "mode", "field",)
    search_fields = ("customer__customer_id", "screen", "mode", "field", )

admin.site.register(FieldEventData, FieldEventDataAdmin)
