from django.db import models


class TransactionCategoriesChoices(models.TextChoices):
    withdraw = "WITHDRAW", "Withdraw"
    deopsit = "DEPOSIT", "Deposit"