from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False)


class PasswordReset(models.Model):
    is_used = models.BooleanField(default=False)
    token = models.CharField(max_length=100)
    expiry_time = models.DateTimeField(
        default=timezone.now() + timedelta(minutes=10)
    )
  
    user = models.ForeignKey("User", on_delete=models.CASCADE)
