from django.contrib import admin
from CORE_APP.models import FooterModel
# Register your models here.

@admin.register(FooterModel)
class FooterModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'open_in_new_tab', 'created_by', 'updated_at')
    list_filter = ('parent', 'created_by', 'updated_at')
    search_fields = ('title', 'url')
    ordering = ('order', 'title')

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'url', 'parent', 'order', 'open_in_new_tab')
        }),
        ('Appearance', {
            'fields': ('icon', 'icon_image', 'color', 'font_size', 'font_family')
        }),
        ('Audit', {
            'fields': ('created_by', 'updated_by', 'created_at', 'updated_at')
        }),
    )

    readonly_fields = ('slug', 'created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        """Automatically set created_by/updated_by"""
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)