from django.urls import path

from .views import TransactionView, TransactionDetailView, RevertTRansactionView

urlpatterns = [
    path('', TransactionView.as_view(), name='transaction_list'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction-retrieve'),
    path('revert-transaction/<int:pk>/', RevertTRansactionView.as_view(), name='revert_transaction'),
]
