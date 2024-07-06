from django.db import models
from django.contrib.auth.models import AbstractUser

from . user_manager import UserManager


class User(AbstractUser):
    address = models.CharField(max_length=250)

    objects = UserManager()
