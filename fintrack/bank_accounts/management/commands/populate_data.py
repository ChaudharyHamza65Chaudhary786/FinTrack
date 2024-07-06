import datetime

from django.core.management.base import BaseCommand

from bank_accounts.models import  BankAccount
from banks.models import Bank, BankBranch
from transactions.models import  Category, SubCategory
from transactions.transaction_helper import create_transaction, delete_transaction
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):     
        user = User.objects.create(username='hamza65', password='hamza')
       
        bank = Bank.objects.create(name="HBL")
        branch = BankBranch.objects.create(bank=bank, branch_name="JT", branch_code="0169")
        bank_acc = BankAccount.objects.create(
            branch=branch,
            current_balance=1200, 
            acc_number="100", 
            acc_holder_name="hamza", 
            acc_type="Current", 
            acc_holder=user
        )


        income = Category.objects.create(name="Income")
        expense = Category.objects.create(name="Expense") 

        food = SubCategory.objects.create(sub_category="food", category=expense)

        wage = SubCategory.objects.create(sub_category="wage", category=income)

        trans1 = create_transaction("first transaction",datetime.date(2023,10,5),500, bank_acc, "Expense", "food")

        trans2 = create_transaction("secondst transaction",datetime.date(2023,10,5),5000, bank_acc, "Income", "wage")

        delete_transaction(trans2)
