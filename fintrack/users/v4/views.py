from decouple import config
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.models import PasswordReset, User
from users.serializer import UserSerializer, ResetPasswordRequestSerializer, ResetPasswordSerializer
from users.tasks import send_password_reset_email


class RegistrationAPIView(CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ResetPasswordRequest(CreateAPIView):
    serializer_class = ResetPasswordRequestSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, email=request.data['email'])
        
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        
        PasswordReset.objects.create(email=request.data['email'], token=token)

        reset_url = f"{config('PASSWORD_RESET_BASE_URL')}{token}"

        send_password_reset_email.delay(self.request.data['email'], reset_url)
        return Response({"success": "Email sent with forget password link"})
    

class ResetPasswordConfirm(CreateAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        reset_object = PasswordReset.objects.get(token=kwargs['token'])
        if not reset_object or timezone.now() > reset_object.expiry_time:
            return Response(
                {'error':'Invalid or Expired Link'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.get(email=reset_object.email)
        user.set_password(request.data['new_password'])
        user.save()
        
        reset_object.delete()
        
        return Response({'success':'Password updated'})
