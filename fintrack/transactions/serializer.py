from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Transaction can not be negative")
        return amount


class RevertTransactionSerializer(serializers.Serializer):
    transaction = serializers.PrimaryKeyRelatedField(queryset=Transaction.objects.all())
    amount = serializers.IntegerField()

    def validate(self, attrs):
        if attrs['transaction'].is_reverted:
            raise serializers.ValidationError("Transaction is already reverted")
        if attrs['amount'] <= 0:
            raise serializers.ValidationError("Transaction amount can not be negative")
        
        return attrs
