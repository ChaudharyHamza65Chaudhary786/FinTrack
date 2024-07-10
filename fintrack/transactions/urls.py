# transactions/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import transaction,transaction_detail

urlpatterns = [
    path('transactions/', transaction, name='transaction_list'),
    path('transactions/<int:pk>/', transaction_detail   , name='transaction_detail'),
]
