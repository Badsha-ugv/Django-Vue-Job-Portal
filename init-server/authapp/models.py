# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('candidate', 'Candidate'),
        ('company', 'Company'),
    ]

    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPE_CHOICES,
        default='candidate',
    )

    # email = models.EmailField(blank=True,null=True,unique=True)  # Keep for uniqueness

class Category(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
        return self.name
    
