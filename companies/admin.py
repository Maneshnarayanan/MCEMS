from django.contrib import admin
from .models import Company, Department, Role

# Register Company model with custom admin settings
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'contact_phone', 'created_at', 'updated_at')
    search_fields = ('name', 'contact_email')
    list_filter = ('created_at', 'updated_at')

# Register the model with the admin site




@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')


admin.site.register(Company, CompanyAdmin)