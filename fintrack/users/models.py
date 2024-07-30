from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False)


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
