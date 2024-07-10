from django.db import models


class TransactionCategoriesChoices(models.TextChoices):
    Withdraw = "Withdraw", ("Withdraw")
    Deopsit = "Deposit", ("Deposit")


class AccountCategoryChoices(models.TextChoices):
    Current = "Current", ("Current")
    Saving = "Saving", ("Saving")
