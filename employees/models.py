from django.db import models
from companies.models import Company

class Department(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='roles')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employees')
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance')
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.clock_in.date()}"

class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.start_date} to {self.end_date}"
