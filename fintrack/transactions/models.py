from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    sub_category = models.CharField(max_length=50, blank=False, unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category


class Transaction(models.Model):
    description = models.CharField(max_length=300, blank=True)

    date = models.DateField(blank=False)

    amount = models.PositiveIntegerField(blank=False)

    transaction_from_account = models.ForeignKey("bank_accounts.BankAccount", on_delete=models.CASCADE)
    sub_category = models.ForeignKey("transactions.SubCategory", on_delete=models.CASCADE)
    
    