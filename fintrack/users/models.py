from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    address = models.CharField(max_length=250)
    email = models.EmailField(unique=True, blank=False)


class PasswordReset(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=100)
    expiry_time= models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id: 
            self.expiry_date = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)
