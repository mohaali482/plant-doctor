from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['email','first_name', 'last_name', 'is_staff', 'is_active',]
    list_filter = ['is_staff', 'is_active']
    readonly_fields = ['created_at', 'updated_at',]
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password'
                )
            }
        ),
        ('Personal info', {
            'fields': (
                'first_name',
                'last_name',
                ),
            }
        ),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
                )
            }
        ),
        ('Important dates', {'fields': ('last_login','created_at', 'updated_at',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ("groups", "user_permissions",)

admin.site.register(User, UserAdmin)
