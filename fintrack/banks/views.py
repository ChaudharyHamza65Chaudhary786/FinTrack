from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView

from .models import Bank    
from .serializer import BankSerializer, BranchSerializer
from .permissions import StaffOnly


class BankAPIView(ListCreateAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [StaffOnly]


class BankDetailAPIView(RetrieveAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    permission_classes = [StaffOnly]


class BranchAPIView(CreateAPIView):
    serializer_class = BranchSerializer
    permission_classes = [StaffOnly]
