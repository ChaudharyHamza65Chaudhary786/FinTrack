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
    

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, max_length=128)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Both Passwords must be same")
        return attrs 
