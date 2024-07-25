from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from transactions.models import Transaction
from transactions.helper import TransactionManager
from transactions.serializer import RevertTransactionSerializer, TransactionSerializer

transaction_manager = TransactionManager()


class TransactionAPIView(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(
            transaction_from_account__in=self.request.user.bank_accounts.all()
        )
    
    def perform_create(self, serializer):
        transaction_manager.handle_new_transaction(serializer.validated_data)

    
class TransactionDetailAPIView(RetrieveAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class RevertTransactionAPIView(CreateAPIView):
    serializer_class = RevertTransactionSerializer

    def perform_create(self, serializer):
        transaction_manager.handle_revert_transaction(
            serializer.validated_data['transaction'], 
            serializer.validated_data['amount']
        )
