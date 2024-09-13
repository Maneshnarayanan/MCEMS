from .models import Company
from django.shortcuts import render, redirect
from .forms import CompanyForm
from django.shortcuts import get_object_or_404

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