from django.db import models
from django.utils.translation import gettext_lazy as _


class TransactionCategoriesChoices(models.TextChoices):
    Withdrawl = "Withdrawl", _("Withdrawl")
    Deopsit = "Deposit", _("Deposit")


class AccountCategoryChoices(models.TextChoices):
    Current = "Current", _("Current")
    Saving = "Saving", _("Saving")
