from django.urls import path
from rest_framework_simplejwt import views

from . views import UserRegistrationView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]
