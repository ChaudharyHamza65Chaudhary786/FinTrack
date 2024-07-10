
from . models import Transaction
from accounts.models import Account
from accounts.account_helper import AccountHelper


WITHDRAWAL_CATEGORY = "withdrawal"


class TransactionManager():
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
        if transaction_updated_data["category"] == WITHDRAWAL_CATEGORY:
            self.account_helper.deduct_amount(
                account, 
                transaction_updated_data["amount"]
            )
        else:
            self.account_helper.add_amount(
                account, 
                transaction_updated_data["amount"]
            )

    def handle_new_transaction(self, transaction_updated_data):
         self.create_transaction(transaction_updated_data)
         self.update_balance_on_transaction_creation(
             transaction_updated_data["transaction_from_account"], 
             transaction_updated_data
         )
        
    def delete_transaction(self, transaction):
        
        if transaction.category == WITHDRAWAL_CATEGORY:
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

    def update_transaction(self, transaction_to_update, transaction_updated_data):
        self.update_balance_if_account_changed(
            transaction_to_update, 
            transaction_updated_data
        )
        self.update_balance_if_category_changed(
            transaction_to_update, 
            transaction_updated_data
        )
        self.update_balance_if_amount_changed(
            transaction_to_update, 
            transaction_updated_data
        )
        transaction_to_update.description = transaction_updated_data["description"]
        transaction_to_update.date = transaction_updated_data["date"]
        transaction_to_update.amount = transaction_updated_data["amount"]
        transaction_to_update.category = transaction_updated_data["category"]
        transaction_to_update.save()

    def update_balance_if_account_changed(self, transaction_to_update, transaction_updated_data):
        
        if (transaction_to_update.transaction_from_account 
            != transaction_updated_data["transaction_from_account"]):

                new_account = transaction_updated_data["transaction_from_account"]
                current_account = transaction_to_update.transaction_from_account

                if transaction_to_update.category == WITHDRAWAL_CATEGORY:
                    self.account_helper.add_amount(
                        current_account, 
                        transaction_to_update.amount
                    )
                    self.account_helper.deduct_amount(
                        new_account, 
                        transaction_to_update.amount
                    )
                else:
                    self.account_helper.deduct_amount(
                        current_account, 
                        transaction_to_update.amount
                    )
                    self.account_helper.add_amount(
                        new_account, 
                        transaction_to_update.amount
                    )            
                current_account = new_account
    
    def update_balance_if_category_changed(self, transaction_to_update, transaction_updated_data):
            previous_category = transaction_to_update.category
            current_account = transaction_to_update.transaction_from_account

            if previous_category != transaction_updated_data["category"]:

                if transaction_updated_data["category"] == WITHDRAWAL_CATEGORY:
                    self.account_helper.deduct_amount(
                        current_account, 
                        2*transaction_to_update.amount 
                    )
                else:
                    self.account_helper.add_amount(
                        current_account, 
                        2*transaction_to_update.amount
                    )

    def update_balance_if_amount_changed(self, transaction_to_update, transaction_updated_data):
        amount_difference = transaction_to_update.amount - transaction_updated_data["amount"]
        current_account = transaction_to_update.transaction_from_account

        if amount_difference != 0:

            if transaction_updated_data["category"] == WITHDRAWAL_CATEGORY:
                self.account_helper.add_amount(
                    current_account, 
                    amount_difference
                )
            else:
                self.account_helper.deduct_amount(
                    current_account, 
                    amount_difference
                )
