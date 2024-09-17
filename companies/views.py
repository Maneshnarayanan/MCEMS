from .models import Company
from django.shortcuts import render, redirect
from .forms import CompanyForm
from django.shortcuts import get_object_or_404
from .models import Company, Department, Role
from .forms import DepartmentForm, RoleForm

def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/company_form.html', {'form': form})

def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/company_form.html', {'form': form})

from django.shortcuts import redirect

def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'company/company_confirm_delete.html', {'company': company})



# CRUD views for Department

def department_list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    departments = company.departments.all()  # Use related_name from ForeignKey
    return render(request, 'company/department/department_list.html', {'company': company, 'departments': departments})

def create_department(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.company = company
            department.save()
            return redirect('department_list', company_id=company.id)
    else:
        form = DepartmentForm()
    return render(request, 'company/department/department_form.html', {'form': form, 'company': company})

def update_department(request, pk, company_id):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list', company_id=company_id)
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'company/department/department_form.html', {'form': form})

def delete_department(request, pk, company_id):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list', company_id=company_id)
    return render(request, 'company/department/department_confirm_delete.html', {'department': department})

# CRUD views for Role

def role_list(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    roles = company.roles.all()  # Use related_name from ForeignKey
    return render(request, 'company/role/role_list.html', {'company': company, 'roles': roles})

def create_role(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            role = form.save(commit=False)
            role.company = company
            role.save()
            return redirect('role_list', company_id=company.id)
    else:
        form = RoleForm()
    return render(request, 'company/role/role_form.html', {'form': form, 'company': company})

def update_role(request, pk, company_id):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('role_list', company_id=company_id)
    else:
        form = RoleForm(instance=role)
    return render(request, 'company/role/role_form.html', {'form': form})

def delete_role(request, pk, company_id):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        role.delete()
        return redirect('role_list', company_id=company_id)
    return render(request, 'company/ role/role_confirm_delete.html', {'role': role})


