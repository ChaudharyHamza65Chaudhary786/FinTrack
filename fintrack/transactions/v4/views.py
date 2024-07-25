from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from transactions.models import Transaction
from transactions.serializer import TransactionSerializer, TransactionRevertSerializer
from transactions.helper import TransactionManager

transaction_manager = TransactionManager()


class TransactionView(ListCreateAPIView,RetrieveAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            transaction_from_account__in=self.request.user.bank_accounts.all()
        )
    
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        transaction_manager.handle_new_transaction(serializer.validated_data)
        return Response(serializer.data)

    
class TransactionDetailView(RetrieveAPIView):
     
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class RevertTRansactionView(CreateAPIView):
    serializer_class = TransactionRevertSerializer
    
    def get_object(self):
        pk = pk=self.kwargs['pk']
        return get_object_or_404(Transaction, pk=pk)

    def perform_create(self, serializer):
        transaction_manager.handle_revert_transaction(self.get_object(), self.request.data['amount'])
        return Response(
            {"message": "Reverted Successfully"}
        )
