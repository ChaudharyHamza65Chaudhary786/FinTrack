from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .serializer import AccountSerializer
from .models import Account


class AccountAPIView(ListCreateAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(
            holder=self.request.user
        )
