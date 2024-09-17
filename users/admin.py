from users.decorators import role_required

@role_required(['ADMIN'])
def admin_view(request):
    # Only admins can access this view
    pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the admin interface
    list_display = ('username', 'email', 'first_name', 'last_name', 'company', 'role', 'is_staff')
    
    # Add filtering options in the admin interface
    list_filter = ('role', 'company', 'is_staff')
    
    # Add search functionality for users
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Define the fields that are editable in the detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Company & Role', {'fields': ('company', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Define the fields when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'company', 'role'),
        }),
    )
