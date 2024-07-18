from django.urls import path
from rest_framework_simplejwt import views

from . views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', views.TokenObtainPairView.as_view(), name='login'),
]
