from django.contrib import admin
from messenger.models import EmailVerification, Otp, PreSignupData, Notification


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("customer", "email_id", "email_type", "verification_code", "is_verified",
                    "times", "created_at", "updated_at",)
    list_filter = ("email_type",)
    search_fields = ("customer__customer_id", "email_id", "email_type", "verification_code", "is_verified",
                     "times", "created_at", "updated_at", )

admin.site.register(EmailVerification, EmailVerificationAdmin)


class OtpAdmin(admin.ModelAdmin):
    list_display = ("customer", "mobile_number",
                    "otp_code", "times", "is_verified", "created_at", "updated_at",)
    search_fields = ("customer__customer_id", "mobile_number", "otp_code",
                     "times", "is_verified", "created_at", "updated_at", )

admin.site.register(Otp, OtpAdmin)


class PreSignupDataAdmin(admin.ModelAdmin):
    list_display = ("app_registration_id", "imei", "created_at", "updated_at",)
    search_fields = ("app_registration_id", "imei",
                     "created_at", "updated_at", )

admin.site.register(PreSignupData, PreSignupDataAdmin)


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message_title", "message_body", "data_message",
                    "notification_type", "created_at", "updated_at",)
    search_fields = ("message_title", "message_body", "data_message",
                     "notification_type", "created_at", "updated_at", )

admin.site.register(Notification, NotificationAdmin)
