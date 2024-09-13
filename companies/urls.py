from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/update/<int:pk>/', views.update_company, name='update_company'),
    path('companies/delete/<int:pk>/', views.delete_company, name='delete_company'),
]
