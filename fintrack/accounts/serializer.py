from rest_framework import serializers

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, data):
        if data['current_balance'] < 0:
            raise serializers.ValidationError("Balance can not be negative")
        return data
