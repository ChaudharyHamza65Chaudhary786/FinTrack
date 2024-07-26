from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
from django.http import HttpResponseForbidden

from .models import Bank, Branch
from .serializer import BankSerializer, BranchSerializer


class BankAPIView(ListCreateAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Permssion Denied")

        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Permssion Denied")
        
        return super().create(request, *args, **kwargs)
    

class BankDetailAPIView(RetrieveAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all() 


class BranchAPIView(CreateAPIView):
    serializer_class = BranchSerializer

