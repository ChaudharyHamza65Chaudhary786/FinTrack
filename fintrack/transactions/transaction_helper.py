from django.db import transaction

from . models import Transaction
from accounts.account_helper import AccountHelper

WITHDRAW_CATEGORY = "WITHDRAW"
DEPOSIT_CATEGORY = "DEPOSIT"


class TransactionManager:
    account_helper = AccountHelper()

    @transaction.atomic
    def handle_revert_transaction(self, transaction_to_revert, new_amount=None):
        transaction_data = {
            "description": transaction_to_revert.description,
            "date": transaction_to_revert.date, 
            "amount": transaction_to_revert.amount,
            "transaction_from_account": transaction_to_revert.transaction_from_account,
            "category": transaction_to_revert.category,  
        }
        if new_amount:
            transaction_data["amount"] = new_amount
            self.handle_new_transaction(transaction_data)
            
        transaction_data["amount"] = -(transaction_to_revert.amount)
        self.handle_new_transaction(transaction_data)
        
    @transaction.atomic
    def handle_new_transaction(self, transaction_updated_data):
         self.create_transaction(transaction_updated_data)
         self.update_balance_on_transaction_creation(
            transaction_updated_data["transaction_from_account"], 
            transaction_updated_data
         )
           
    def create_transaction(self, transaction_data):
        Transaction.objects.create(
            description=transaction_data["description"], 
            date=transaction_data["date"],
            amount=transaction_data["amount"], 
            transaction_from_account=transaction_data["transaction_from_account"], 
            category=transaction_data["category"]
        )  
    
    def update_balance_on_transaction_creation(self, account, transaction_updated_data):
        if transaction_updated_data["category"] == WITHDRAW_CATEGORY:
            self.account_helper.deduct_amount(
                account,        
                transaction_updated_data["amount"]
            )
        else:
            self.account_helper.add_amount(
                account, 
                transaction_updated_data["amount"]
            )
