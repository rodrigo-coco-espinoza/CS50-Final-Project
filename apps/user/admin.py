from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserAccount

@admin.register(UserAccount)
class CustomUserAdmin(BaseUserAdmin):
    model = UserAccount
    list_display = ('username', 'is_staff', 'is_pc_isla_editor', 'is_pc_isla_admin', 'is_pc_isla_investigador', 'persona',)
    search_fields = ('username', 'is_staff', 'is_pc_isla_editor', 'is_pc_isla_admin', 'is_pc_isla_investigador', 'persona',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_pc_isla_editor', 'is_pc_isla_admin', 'is_pc_isla_investigador', 'persona', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_active', 'is_staff', 'is_pc_isla_editor', 'is_pc_isla_admin', 'is_pc_isla_investigador', 'persona', 'is_superuser'),
        }),
    )
