from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from . models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Transaction Can not be negative")
        return amount


class TransactionRevertSerializer(serializers.Serializer):
    amount = serializers.IntegerField()

    def validate(self, attrs):
        transaction_id = self.context.get('view').kwargs['pk']
        
        transaction = get_object_or_404(
            Transaction, 
            pk=transaction_id, 
        )
        if transaction.is_reverted:
            raise serializers.ValidationError("Transaction is already reverted")
        
        return attrs

