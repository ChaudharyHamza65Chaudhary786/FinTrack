from rest_framework.generics import CreateAPIView

from users.serializer import UserSerializer


class RegistrationAPIView(CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = []
