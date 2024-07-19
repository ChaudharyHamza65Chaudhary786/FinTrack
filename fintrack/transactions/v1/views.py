from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response    

from transactions.models import Transaction
from transactions.serializer import TransactionSerializer
from transactions.transaction_helper import TransactionManager

transaction_manager = TransactionManager()


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def transaction(request):
    response = None 

    if request.method == 'GET':
        transactions = Transaction.objects.filter(transaction_from_account__in=request.user.bank_accounts.all())

        paginator = PageNumberPagination()
        paginated_transactions = paginator.paginate_queryset(transactions, request)

        serializer = TransactionSerializer(paginated_transactions, many=True)
        response = paginator.get_paginated_response(serializer.data)
    else:
        if request.data["amount"] < 0:
            response = Response(
                "Transaction Can not be negative", 
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            serializer = TransactionSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            transaction_manager.handle_new_transaction(serializer.validated_data)
            response = Response(serializer.data)    
            
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, transaction_from_account__holder=request.user)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revert_transaction(request, pk):
    response = None
    transaction = get_object_or_404(Transaction, pk=pk, transaction_from_account__holder=request.user)

    if transaction.amount < 0:
        response = Response(
            "Can not revert this transaction", 
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        transaction_manager.handle_revert_transaction(transaction, request.data)
        response = Response("Reverted Successfully")
    return response
