from django.db import models
from django.utils.translation import gettext_lazy as _


from banks.models import Branch
from choices import AccountCategoryChoices
from users.models import User


class Account(models.Model):
   

    holder_name = models.CharField(max_length=100)
    acc_number = models.CharField(max_length=20, primary_key=True)
    category = models.CharField(choices=AccountCategoryChoices.choices, max_length=100)

    current_balance = models.PositiveBigIntegerField()

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    holder = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch} {self.holder_name } {self.acc_number}"
