from django.urls import path

from .views import TransactionAPIView, TransactionDetailAPIView, RevertTransactionAPIView, TransactionReportAPIView

urlpatterns = [
    path('', TransactionAPIView.as_view(), name='transaction_list'),
    path('<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-retrieve'),
    path('revert-transaction/', RevertTransactionAPIView.as_view(), name='revert_transaction'),
    path('generate-report/', TransactionReportAPIView.as_view(), name='generate_report')
]
