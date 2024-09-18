from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),  
    path('home/', views.home, name='home'),
    path('profile/', views.profile_view, name='employee-profile'),
]
