from django.db import models


class TransactionCategoriesChoices(models.TextChoices):
    WITHDRAW = "WITHDRAW", "Withdraw"
    DEPOSIT = "DEPOSIT", "Deposit"
