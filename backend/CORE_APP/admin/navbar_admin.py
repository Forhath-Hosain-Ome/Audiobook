from django.contrib import admin
from CORE_APP.models import NavbarModel
# Register your models here.


@admin.register(NavbarModel)
class NavbarModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'order', 'is_dropdown', 'open_in_new_tab', 'created_by', 'updated_at')
    list_filter = ('is_dropdown', 'parent', 'visible_to_roles', 'created_by', 'updated_at')
    search_fields = ('title', 'url')
    ordering = ('order', 'title')
    filter_horizontal = ('visible_to_roles',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'url', 'parent', 'order', 'is_dropdown', 'open_in_new_tab')
        }),
        ('Appearance', {
            'fields': ('icon', 'icon_image', 'color', 'font_size', 'font_family')
        }),
        ('Permissions', {
            'fields': ('visible_to_roles',)
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