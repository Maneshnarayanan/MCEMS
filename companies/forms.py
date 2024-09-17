from django import forms
from .models import Company
from .models import Department, Role

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'contact_email', 'contact_phone', 'logo']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'company']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'company']