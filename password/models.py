from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.site_name