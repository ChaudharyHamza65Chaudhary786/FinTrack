import datetime

from django.core.management.base import BaseCommand

from accounts.models import  Account
from banks.models import Bank, Branch
from transactions.helper import TransactionManager
from users.models import User

transaction_manager = TransactionManager()


class Command(BaseCommand):

    def create_transaction_data(self, description, date, amount, account, category):
        return {
            "description": description,
            "date": date,
            "amount": amount,
            "transaction_from_account": account,
            "category": category
        }

        def handle(self, *args, **kwargs):     
            user, _ = User.objects.get_or_create(username='ali')   
            bank, _ = Bank.objects.get_or_create(name="HBL")
            branch, _  = Branch.objects.get_or_create(
                bank=bank, 
                name="JT", 
                code="0169", 
                address=" Johar town, Lahore", 
                phone_number="042-35315101"
        )

        account, _ = Account.objects.get_or_create(
            branch=branch,
            current_balance=1200, 
            number="200", 
            title="ali", 
            category="CURRENT", 
            holder=user
        )

        # trans1 = transaction_manager.handle_new_transaction(
        #     self.create_transaction_data(
        #         "first transaction", 
        #         datetime.date(2023, 10, 5), 
        #         500, 
        #         account, 
        #         "WITHDRAW"
        #     )
        # )
        
        # trans2 = transaction_manager.handle_new_transaction(
        #     self.create_transaction_data(
        #         "secondst transaction", 
        #         datetime.date(2023, 10, 5), 
        #         5000, 
        #         account, 
        #         "DEPOSIT"
        #     )
        # )
        # acc = Account.objects.get(number="200")
        # acc_1 = Account.objects.get(number="100")
        # print(acc.current_balance, acc_1.current_balance)
