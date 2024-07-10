import datetime


from django.core.management.base import BaseCommand


from accounts.models import  Account
from banks.models import Bank, Branch
from transactions.transaction_helper import create_transaction, delete_transaction
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):     
        user, _ = User.objects.get_or_create(username='hamza65', password='hamza')
       
        bank, _ = Bank.objects.get_or_create(name="HBL")
        branch, _  = Branch.objects.get_or_create(bank=bank, name="JT", code="0169", address=" Johar town, Lahore", phone_number="042-35315101")
        account, _ = Account.objects.get_or_create(
            branch=branch,
            current_balance=1200, 
            number="200", 
            title="hamza", 
            category="Current", 
            holder=user
        )

        trans1 = create_transaction("first transaction",datetime.date(2023,10,5),500, account, "Withdraw")

        trans2 = create_transaction("secondst transaction",datetime.date(2023,10,5),5000, account, "Deposit")
        acc = Account.objects.get(number="200")
        acc_1 = Account.objects.get(number="100")
        print(acc.current_balance, acc_1.current_balance)

