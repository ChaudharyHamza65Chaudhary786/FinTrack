from django.urls import path

from .views import BankAPIView, BranchAPIView, BankDetailAPIView

urlpatterns = [
    path('', BankAPIView.as_view(), name='banks'),
    path('create-branch/', BranchAPIView.as_view(), name='create_branch'),
    path('<int:pk>/', BankDetailAPIView.as_view(), name='bank_details')
]
