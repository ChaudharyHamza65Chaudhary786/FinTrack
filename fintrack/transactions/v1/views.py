from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response    

from transactions.models import Transaction
from transactions.serializer import TransactionSerializer
from transactions.helper import TransactionManager

transaction_manager = TransactionManager()


@api_view(['GET', 'POST'])
def transaction(request):

    if request.method == 'GET':
        transactions = Transaction.objects.filter(transaction_from_account__in=request.user.bank_accounts.all())

        paginator = PageNumberPagination()
        paginated_transactions = paginator.paginate_queryset(transactions, request)

        serializer = TransactionSerializer(paginated_transactions, many=True)
        response = paginator.get_paginated_response(serializer.data)
        
    else:
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction_manager.handle_new_transaction(serializer.validated_data)
        response = Response(serializer.data)    
            
    return response


@api_view(['GET'])
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, transaction_from_account__holder=request.user)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)


@api_view(['POST'])
def revert_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, transaction_from_account__holder=request.user)

    if transaction.is_reverted:
        response = Response(
                { "message": " Can not revert this transaction"}, 
                status= status.HTTP_400_BAD_REQUEST
            )
    else:
        transaction_manager.handle_revert_transaction(transaction, request.data)
        response = Response(
                { "message": "Reverted Successfully"}
            )
    return response
