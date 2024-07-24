class AccountHelper:
    def deduct_amount(self, account, amount):
        account.current_balance = account.current_balance - amount
        account.save()

    def add_amount(self, account, amount):
        account.current_balance = account.current_balance + amount
        account.save()
