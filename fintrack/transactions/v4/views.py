from django.http import FileResponse
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, ListAPIView

from transactions.filters import TransactionFilter
from transactions.helper import TransactionManager
from transactions.models import Transaction
from transactions.serializer import RevertTransactionSerializer, TransactionSerializer

transaction_manager = TransactionManager()


class TransactionAPIView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter

    def get_queryset(self):
        return Transaction.objects.filter(
            transaction_from_account__holder=self.request.user
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


class TransactionReportAPIView(ListAPIView):
    serializer_class = TransactionSerializer
    filterset_class = TransactionFilter
    pagination_class = None

    def get_queryset(self):
        return Transaction.objects.filter(
            transaction_from_account__holder=self.request.user
        )
    
    def get(self, request, *args, **kwargs):
        response = self.list(request, *args, **kwargs)
        report_buffer = transaction_manager.generate_transaction_report(response.data)
        return FileResponse(report_buffer, as_attachment=True, filename='transaction_report.pdf')
