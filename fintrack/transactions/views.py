from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from . models import Transaction
from . serializer import TransactionSerializer
from . transaction_helper import TransactionManager


transaction_manager = TransactionManager()


@api_view(['GET', 'POST'])
def transaction(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response (serializer.data)
    
    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction_manager.handle_new_transaction(serializer.validated_data)
        else:
            print(serializer.errors)
        return Response(serializer.data)


@api_view(['GET'])
def transaction_detail(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction)
        return Response (serializer.data)


@api_view([ 'PUT', 'DELETE'])
def manage_transaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
        if "REVERTED" in transaction.description:
            raise ValueError("Can not update a reverted transaction")
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            transaction_manager.update_transaction(transaction, serializer.validated_data)
            return Response(serializer.data)     
        else:
            print(serializer.errors)

    else:
        transaction_manager.delete_transaction(transaction)
        return Response.status_code(status=status.HTTP_204_NO_CONTENT)
