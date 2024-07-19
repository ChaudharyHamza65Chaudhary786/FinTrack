from rest_framework import serializers

from . models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'address')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            address=validated_data['address']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
