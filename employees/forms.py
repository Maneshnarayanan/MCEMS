from django import forms
from .models import Employee, LeaveRequest

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'department', 'role', 'joining_date', 'salary']

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason']
