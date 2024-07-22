from rest_framework import serializers

from . models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Transaction Can not be negative")
        