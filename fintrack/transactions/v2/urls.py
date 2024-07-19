from django.urls import path

from .views import TransactionView, TransactionDetailView, RevertTransactionView

urlpatterns = [
    path('', TransactionView.as_view(), name='transaction_list'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('revert-transaction/<int:pk>/', RevertTransactionView.as_view(), name='revert_transaction'),
]
