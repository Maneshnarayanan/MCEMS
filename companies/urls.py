from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/update/<int:pk>/', views.update_company, name='update_company'),
    path('companies/delete/<int:pk>/', views.delete_company, name='delete_company'),


    # Department URLs
    path('company/<int:company_id>/departments/', views.department_list, name='department_list'),
    path('company/<int:company_id>/departments/create/', views.create_department, name='create_department'),
    path('company/<int:company_id>/departments/<int:pk>/update/', views.update_department, name='update_department'),
    path('company/<int:company_id>/departments/<int:pk>/delete/', views.delete_department, name='delete_department'),
    

    # Role URLs
    path('company/<int:company_id>/roles/', views.role_list, name='role_list'),
    path('company/<int:company_id>/roles/create/', views.create_role, name='create_role'),
    path('company/<int:company_id>/roles/<int:pk>/update/', views.update_role, name='update_role'),
    path('company/<int:company_id>/roles/<int:pk>/delete/', views.delete_role, name='delete_role'),

    
]
