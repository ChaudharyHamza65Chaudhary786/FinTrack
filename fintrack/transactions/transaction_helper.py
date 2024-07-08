
from . models import Transaction
from accounts.bank_account_helper import AccountHelper


WITHDRAWL_CATEGORY = "Withdrawl"

def create_transaction(description, date, amount, account, category):

    bank_acc = account
    transaction = Transaction.objects.create(date=date, amount=amount, transaction_from_account=bank_acc, category=category)
    if category == WITHDRAWL_CATEGORY:
        AccountHelper.deduct_amount(bank_acc, amount)
    else:
        AccountHelper.add_amount(bank_acc, amount)
    return transaction

def delete_transaction(transaction):
    bank_acc = transaction.transaction_from_account
    if transaction.category== WITHDRAWL_CATEGORY:
        AccountHelper.add_amount(bank_acc, transaction.amount)
    else:
        AccountHelper.deduct_amount(bank_acc, transaction.amount)
    transaction.delete()
