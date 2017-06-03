from django.contrib import admin
from pan.models import Pan


class PanAdmin(admin.ModelAdmin):
    list_display = ("customer", "pan", "is_verified", "title",
                    "first_name", "middle_name", "last_name", "father_first_name", "father_middle_name",
                    "father_last_name", "dob", "status", "pan_updates", "created_at", "updated_at",)
    search_fields = ("customer__customer_id", "pan", "is_verified", "title",
                     "first_name", "middle_name", "last_name", "father_first_name", "father_middle_name",
                     "father_last_name", "dob", "status", "pan_updates", "created_at", "updated_at", )

admin.site.register(Pan, PanAdmin)
