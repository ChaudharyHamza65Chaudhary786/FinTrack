from django.urls import path
from rest_framework_simplejwt import views

from . views import UserRegistrationAPIView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
]
