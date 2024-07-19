from django.urls import path
from rest_framework_simplejwt import views

from . views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('token/', views.TokenObtainPairView.as_view(), name='token_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh')
]
