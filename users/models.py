from django.contrib.auth.models import AbstractUser
from django.db import models
from companies.models import Company

class User(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='users_in_company')

    ADMIN = 'ADMIN'
    HR_MANAGER = 'HR_MANAGER'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (HR_MANAGER, 'HR Manager'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)

    def __str__(self):
        return self.username
