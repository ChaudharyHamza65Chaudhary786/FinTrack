
from . models import Transaction
from fintrack.accounts.account_helper import AccountHelper


WITHDRAWL_CATEGORY = "Withdrawl"

def create_transaction(description, date, amount, account, category):

    account = account
    transaction = Transaction.objects.create(date=date, amount=amount, transaction_from_account=account, category=category)
    if category == WITHDRAWL_CATEGORY:
        AccountHelper.deduct_amount(account, amount)
    else:
        AccountHelper.add_amount(account, amount)
    return transaction

def delete_transaction(transaction):
    account = transaction.transaction_from_account
    if transaction.category== WITHDRAWL_CATEGORY:
        AccountHelper.add_amount(account, transaction.amount)
    else:
        AccountHelper.deduct_amount(account, transaction.amount)
    transaction.delete()
