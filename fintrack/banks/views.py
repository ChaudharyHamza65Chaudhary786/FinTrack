from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.http import HttpResponseForbidden

from .models import Bank, Branch
from .serializer import BankSerializer, BranchSerializer


class BankViewApi(ListCreateAPIView):
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
    

class BrachAPIView(ListCreateAPIView):
    serialzer_class = BranchSerializer

    def get_queryset(self):
        return Branch.objects.filter(
            bank__name=self.kwargs['bank']
        )
