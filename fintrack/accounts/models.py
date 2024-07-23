from django.db import models

from banks.models import Branch
from .choices import AccountCategoryChoices
from users.models import User


class Account(models.Model):
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=20, primary_key=True)
    category = models.CharField(choices=AccountCategoryChoices.choices, max_length=100)
    current_balance = models.PositiveBigIntegerField()

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_accounts")

    def __str__(self):
        return f"{self.branch} {self.title } {self.number}"
