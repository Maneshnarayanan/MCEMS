from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/create/', views.create_employee, name='create_employee'),
    path('employee/update/<int:pk>/', views.update_employee, name='update_employee'),
    path('employee/delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('attendance/clock_in/', views.record_attendance, name='record_attendance'),
    path('attendance/clock_out/<int:pk>/', views.clock_out_attendance, name='clock_out_attendance'),
    path('leave_request/', views.leave_request, name='leave_request'),
]
