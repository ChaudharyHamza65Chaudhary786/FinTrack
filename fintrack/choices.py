from django.db import models


class TransactionCategoriesChoices(models.TextChoices):
    withdraw = "WITHDRAW", "Withdraw"
    deopsit = "DEPOSIT", "Deposit"


class AccountCategoryChoices(models.TextChoices):
    current = "CURRENT", "Current"
    saving = "SAVING", "Saving"
