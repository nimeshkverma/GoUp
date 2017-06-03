from django.contrib import admin
from documents.models import Documents, DocumentType


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ("customer", "document_type", "document_1", "document_2", "document_3",
                    "document_4", "document_5", "document_6", "status", "created_at", "updated_at", "is_active")
    list_filter = ("document_type",)
    search_fields = ("customer__customer_id", "document_type__name",
                     "created_at", "updated_at", )

admin.site.register(Documents, DocumentsAdmin)


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "usage", "created_at", "updated_at", "is_active",)
    search_fields = ("customer__customer_id", "name", "first_name",
                     "usage", "created_at", "updated_at", )

admin.site.register(DocumentType, DocumentTypeAdmin)
