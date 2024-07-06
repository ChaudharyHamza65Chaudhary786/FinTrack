from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class BankBranch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100, unique=True)

    bank = models.ForeignKey("banks.Bank", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch_name} ({self.branch_code})"
    
    @property
    def bank_name(self):
        return self.bank.name
