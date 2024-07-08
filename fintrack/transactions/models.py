from django.db import models
from django.utils.translation import gettext_lazy as _


from choices import TransactionTypeChoices


class Transaction(models.Model):

    description = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=20, choices=TransactionTypeChoices.choices, blank=False)

    date = models.DateField(blank=False)

    amount = models.PositiveIntegerField(blank=False)

    transaction_from_account = models.ForeignKey("accounts.BankAccount", on_delete=models.CASCADE)
