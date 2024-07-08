from django.shortcuts import render
from django.views.generic import ListView

from . models import Transaction

class TransactionsListingView(ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'transactions/list_transactions.html'

    def get_queryset(self):
        return Transaction.objects.filter(transaction_from_account__holder=self.request.user)
