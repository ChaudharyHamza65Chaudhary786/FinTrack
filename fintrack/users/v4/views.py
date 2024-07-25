from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializer import UserSerializer


class RegistrationAPIView(CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
