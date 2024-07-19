from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False)
