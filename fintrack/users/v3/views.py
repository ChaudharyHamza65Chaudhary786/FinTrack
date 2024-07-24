from rest_framework import viewsets
from rest_framework.response import Response

from users.serializer import UserSerializer


class RegistrationViewSet(viewsets.ViewSet):

    permission_classes = []

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.validated_data)
