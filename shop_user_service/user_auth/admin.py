from django.contrib import admin
from .models import User
from django.utils import timezone
from django.contrib import messages


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Resource', {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'bvn', 'birthday'), }),
        ('Others', {
            'fields': ('status', 'last_login', 'created', 'created_by', 'updated',
                    'updated_by', 'is_active', 'deleted_at', 'deleted_by', 'is_deleted'), }),
    ]

    list_display = ('username','is_staff','is_active','is_superuser','first_name', 'last_name', 'email', 'phone_number' )
    list_display_links = ('username','is_staff','is_active','is_superuser','first_name', 'last_name', 'email', 'phone_number' )

    list_filter = ('created', 'updated')
    search_Fields = ('first_name', 'last_name')
    date_hierarchy = 'created'
    ordering = ('-created',)

    # Commom data for all objects
    readonly_fields = [
        'last_login',
        'created',
        'updated',
        'updated_by',
        'is_deleted',
        'deleted_at',
        'deleted_by',
        'created_by',
        'is_active',

    ]

    def has_delete_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.id
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Soft Delete
        data = obj
        if data.is_deleted:
            # If data is already deleted
            return self.message_user(
                request, "This object is already deleted.", level=messages.ERROR)
        data.is_deleted = True
        data.is_active = False

        data.deleted_at = timezone.now()
        data.deleted_by = request.user.id
        data.updated = timezone.now()
        data.updated_by = request.user.id
        data.status = 'Deleted'
        data.save()

        return self.message_user(
            request, "Object is deleted successfully.", level=messages.SUCCESS)
