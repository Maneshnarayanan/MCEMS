from django.contrib import admin
from .models import Employee, Department, Role, Attendance, LeaveRequest

# Register the Employee model with full permissions
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'role', 'company', 'user')
    search_fields = ('name', 'employee_id', 'user__username', 'department__name', 'company__name')
    list_filter = ('department', 'company', 'role')