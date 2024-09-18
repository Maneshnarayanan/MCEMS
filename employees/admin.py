from django.contrib import admin
from .models import Employee, Department, Role, Attendance, LeaveRequest ,User
from django.contrib.auth.admin import UserAdmin


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'role', 'company', 'user')
    search_fields = ('name', 'employee_id', 'user__username', 'department__name', 'company__name')
    list_filter = ('department', 'company', 'role')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'company', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'company', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    def get_employee_profile(self, obj):
        return obj.employee_profile.name if hasattr(obj, 'employee_profile') else 'N/A'
    get_employee_profile.short_description = 'Employee Profile'    

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'clock_in', 'clock_out')
    list_filter = ('employee', 'clock_in')
    search_fields = ('employee__user__first_name', 'employee__user__last_name', 'clock_in')
    date_hierarchy = 'clock_in'

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'reason', 'approved')
    list_filter = ('approved', 'start_date', 'end_date')
    search_fields = ('employee__user__first_name', 'employee__user__last_name', 'reason')
    date_hierarchy = 'start_date'    