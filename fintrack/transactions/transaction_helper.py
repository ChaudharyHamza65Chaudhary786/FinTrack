from django.db import transaction


from . models import Transaction
from accounts.account_helper import AccountHelper


WITHDRAW_CATEGORY = "Withdraw"
DEPOSIT_CATEGORY = "Deposit"


class TransactionManager:
    account_helper = AccountHelper()
       
    def create_transaction(self, transaction_updated_data):    
        Transaction.objects.create(
            description=transaction_updated_data["description"], 
            date=transaction_updated_data["date"],
            amount=transaction_updated_data["amount"], 
            transaction_from_account=transaction_updated_data["transaction_from_account"], 
            category=transaction_updated_data["category"]
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

    @transaction.atomic
    def handle_new_transaction(self, transaction_updated_data):
         self.create_transaction(transaction_updated_data)
         self.update_balance_on_transaction_creation(
             transaction_updated_data["transaction_from_account"], 
             transaction_updated_data
         )
        
    def delete_transaction(self, transaction):
        if transaction.category == WITHDRAW_CATEGORY:
            self.account_helper.add_amount(
                transaction.transaction_from_account, 
                transaction.amount
            )
        else:
            self.account_helper.deduct_amount(
                transaction.transaction_from_account, 
                transaction.amount
            )
        transaction.delete()

    @transaction.atomic
    def update_transaction(self, transaction_to_update, transaction_updated_data):
        self.revert_transaction(transaction_to_update)
        self.handle_new_transaction(transaction_updated_data)

    def revert_transaction(self, transaction_to_revert):
        account = transaction_to_revert.transaction_from_account

        if transaction_to_revert.category == WITHDRAW_CATEGORY:
            self.account_helper.add_amount(
                account,
                transaction_to_revert.amount
            )
        else:
            self.account_helper.deduct_amount(
                account,
                transaction_to_revert.amount
            )

        new_description = (
            f" REVERTED: {transaction_to_revert.description}"
            f"Amount : {transaction_to_revert.amount} ({transaction_to_revert.category})"
        )
        revert_transaction_data = {
            "description": new_description,
            "date": transaction_to_revert.date, 
            "amount": 0,
            "transaction_from_account": transaction_to_revert.transaction_from_account,
            "category": transaction_to_revert.category,  
        }
        self.handle_new_transaction(revert_transaction_data)
