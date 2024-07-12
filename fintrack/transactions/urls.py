from django.urls import path

from .views import transaction, transaction_detail, revert_transaction

urlpatterns = [
    path('transactions/', transaction, name='transaction_list'),
    path('transactions/<int:pk>/', transaction_detail, name='transaction_detail'),
    path('transactions/revert-transaction/<int:pk>/', revert_transaction, name='revert_transaction'),
]
