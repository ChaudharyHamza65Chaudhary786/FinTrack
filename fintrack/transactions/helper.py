import io

from django.db import transaction
from reportlab.pdfgen import canvas

from .models import Transaction
from accounts.helper import AccountHelper

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
            "is_reverted": True
        }
        if new_amount:
            transaction_data["amount"] = new_amount
            self.handle_new_transaction(transaction_data)
            
        transaction_data["amount"] = -(transaction_to_revert.amount)
        self.handle_new_transaction(transaction_data)
        transaction_to_revert.is_reverted = True
        transaction_to_revert.save()
        
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
            category=transaction_data["category"],
            is_reverted=transaction_data.get("is_reverted", False)
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

    def generate_transaction_report(self, transactions):
        buffer = io.BytesIO()

        pdf = canvas.Canvas(buffer)
        pdf.drawString(200, 750, "Transaction Report")

        y_coordinate = 700
        counter = 0
        for transaction in transactions:
            pdf.drawString(100, y_coordinate, f"Transaction ID: {transaction['id']}")
            pdf.drawString(300, y_coordinate, f"Date:: {transaction['date']}")
            pdf.drawString(100, y_coordinate-20, f"Category: {transaction['category']}")
            pdf.drawString(300, y_coordinate-20, f"Amount: {transaction['amount']}")
            pdf.drawString(100, y_coordinate-40, f"Transaction From: {transaction['transaction_from_account']}")
            pdf.drawString(300, y_coordinate-40, f"Description: {transaction['description']}")
            y_coordinate -= 100
            counter += 1

            if counter == 5 : 
                pdf.showPage()
                y_coordinate = 700

        pdf.save()

        buffer.seek(0)
        return buffer
