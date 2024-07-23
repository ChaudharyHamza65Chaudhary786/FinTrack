from django.db import models

from .choices import TransactionCategoriesChoices


class Transaction(models.Model):
    
    is_reverted = models.BooleanField(default=False, blank=True)
    category = models.CharField(
        max_length=20, 
        choices=TransactionCategoriesChoices.choices
    )
    date = models.DateField()
    amount = models.IntegerField()
    description = models.TextField(blank=True)

    transaction_from_account = models.ForeignKey(
        "accounts.Account", 
        on_delete=models.CASCADE,
        related_name="transactions"
    )
