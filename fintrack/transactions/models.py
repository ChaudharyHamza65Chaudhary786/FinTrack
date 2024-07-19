from django.db import models

from .choices import TransactionCategoriesChoices


class Transaction(models.Model):
    description = models.TextField(blank=True)
    
    category = models.CharField(
        max_length=20, 
        choices=TransactionCategoriesChoices.choices
    )

    date = models.DateField()

    amount = models.IntegerField()


    transaction_from_account = models.ForeignKey(
        "accounts.Account", 
        on_delete=models.CASCADE,
        related_name="transactions"
    )
