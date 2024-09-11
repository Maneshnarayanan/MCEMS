from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    contact_email = models.EmailField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)  # For uploading logos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name