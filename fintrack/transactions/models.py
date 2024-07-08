from django.db import models
from django.utils.translation import gettext_lazy as _


from choices import TransactionCategoriesChoices


class Transaction(models.Model):

    description = models.CharField(max_length=300, blank=True)
    category = models.CharField(
        max_length=20, 
        choices=TransactionCategoriesChoices.choices
    )

    date = models.DateField()

    amount = models.PositiveIntegerField()

    transaction_from_account = models.ForeignKey(
        "accounts.Account", 
        on_delete=models.CASCADE
    )
