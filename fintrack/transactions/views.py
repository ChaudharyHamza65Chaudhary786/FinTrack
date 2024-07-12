from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . models import Transaction
from . serializer import TransactionSerializer
from . transaction_helper import TransactionManager

transaction_manager = TransactionManager()


@api_view(['GET', 'POST'])
def transaction(request):
    response = None

    if request.method == 'GET':
        transactions = Transaction.objects.all().filter()

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

            if serializer.is_valid():
                transaction_manager.handle_new_transaction(serializer.validated_data)
                response = Response(serializer.data)
            else:
                response = Response(serializer.errors)
    return response


@api_view(['GET'])
def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)


@api_view(['POST']) 
def revert_transaction(request, pk):
    response = None
    transaction = get_object_or_404(Transaction, pk=pk)

    if transaction.amount < 0:
        response = Response(
            "Can not revert this transaction", 
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        transaction_manager.handle_revert_transaction(transaction, request.data)
        response = Response("Reverted Successfully")
    return response
        print("Got transactions")
