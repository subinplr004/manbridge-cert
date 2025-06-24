from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin-Institute'),
        ('certificate_issuer', 'Certificate Issuer'),
        ('staff', 'Teaching Staff/Intern'),
        ('sales', 'Sales & Marketing'),
        ('front_office', 'Front Office'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
