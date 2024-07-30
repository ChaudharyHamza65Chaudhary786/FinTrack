from django.urls import path

from .views import RegistrationAPIView, ResetPasswordRequest, ResetPasswordConfirm

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('forget_password/', ResetPasswordRequest.as_view(), name='reset_password_request'),
    path('password-reset/<token>/', ResetPasswordConfirm.as_view(), name='reset_password_confirm')
]
