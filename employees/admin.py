from django.contrib import admin
from .models import Employee, Department, Role, Attendance, LeaveRequest

# Register the Employee model with full permissions
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee_id', 'department', 'role', 'joining_date', 'salary')
