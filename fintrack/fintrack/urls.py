"""
URL configuration for fintrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/transactions/', include('transactions.v1.urls')),
    path('api/v2/transactions/', include('transactions.v2.urls')),
    path('api/v3/transactions/', include('transactions.v3.urls')),
    path('api/v4/transactions/', include('transactions.v4.urls')),
    path('api/v1/user/', include('users.v1.urls')),
    path('api/v2/user/', include('users.v2.urls')),
    path('api/v3/user/', include('users.v3.urls')),
    path('api/v4/user/', include('users.v4.urls')),
    path('api/bank/', include('banks.urls'))
]
