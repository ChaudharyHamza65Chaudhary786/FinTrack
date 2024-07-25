from django.urls import path

from .views import transaction, transaction_detail, revert_transaction

urlpatterns = [
    path('', transaction, name='transaction_list'),
    path('<int:pk>/', transaction_detail, name='transaction_detail'),
    path('revert-transaction/', revert_transaction, name='revert_transaction'),
]
