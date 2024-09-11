from django.shortcuts import render, redirect, get_object_or_404
from .models import Company
from .forms import CompanyForm
from django.shortcuts import redirect

# Create or Update a company
def manage_company(request, company_id=None):
    if company_id:
        company = get_object_or_404(Company, id=company_id)
    else:
        company = None
    
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')  # Redirect to the company list after save
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'company/manage_company.html', {'form': form, 'company': company})


# list company
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})


#delete company

def delete_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        company.delete()
        return redirect('company_list')
    return render(request, 'company/confirm_delete.html', {'company': company})