# transactions/urls.py

from django.urls import path
from .views import transaction, transaction_detail, manage_transaction

urlpatterns = [
    path('transactions/', transaction, name='transaction_list'),
    path('transactions/<int:pk>/', transaction_detail, name='transaction_detail'),
    path('transactions/manage-transaction/<int:pk>/', manage_transaction, name='manage_transaction'),
]
