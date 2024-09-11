from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('companies/add/', views.manage_company, name='add_company'),
    path('companies/edit/<int:company_id>/', views.manage_company, name='edit_company'),
    path('companies/delete/<int:company_id>/', views.delete_company, name='delete_company'),
]
