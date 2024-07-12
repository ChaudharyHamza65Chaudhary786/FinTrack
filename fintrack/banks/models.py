from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=14)

    bank = models.ForeignKey("banks.Bank", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.code})"
