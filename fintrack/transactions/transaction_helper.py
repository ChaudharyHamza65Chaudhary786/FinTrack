
from . models import Transaction, Category, SubCategory
from bank_accounts.models import BankAccount


def create_transaction(description, date, amount, acc, cat, sub_cat):
    category = Category.objects.get(name=cat)
    sub_category = SubCategory.objects.get(sub_category=sub_cat)
    bank_acc = acc
    trans1 = Transaction.objects.create(date=date, amount=amount, transaction_from_account=bank_acc, sub_category=sub_category)
    if cat == "Expense":
        deduct_amount(bank_acc, amount)
    else:
        add_amount(bank_acc, amount)
    return trans1

def delete_transaction(transaction):
    bank_acc = transaction.transaction_from_account
    if transaction.sub_category.category == "Expense":
        add_amount(bank_acc, transaction.amount)
    else:
        deduct_amount(bank_acc, transaction.amount)
    transaction.delete()


def deduct_amount(bank_acc, amount):
    bank_acc.current_balance = bank_acc.current_balance - amount
    bank_acc.save()

def add_amount(bank_acc, amount):
    bank_acc.current_balance = bank_acc.current_balance + amount
    bank_acc.save()
