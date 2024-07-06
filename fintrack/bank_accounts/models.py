from django.db import models
from django.utils.translation import gettext_lazy as _


from banks.models import BankBranch
from users.models import User


class BankAccount(models.Model):
    class AccountTypeChoices(models.TextChoices):
        Current = "Current", _("Current")
        Saving = "Saving", _("Saving")


    acc_holder_name = models.CharField(max_length=100, blank=False)
    acc_number = models.CharField(max_length=20, primary_key=True)
    acc_type = models.CharField(choices=AccountTypeChoices.choices, max_length=100, blank=False)

    current_balance = models.PositiveBigIntegerField(blank=False)

    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    acc_holder = models.ForeignKey(User, on_delete=models.CASCADE)
