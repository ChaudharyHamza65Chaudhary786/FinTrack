from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
]
