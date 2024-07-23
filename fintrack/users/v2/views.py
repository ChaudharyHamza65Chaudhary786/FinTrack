from rest_framework.views import APIView
from rest_framework.response import Response

from users.serializer import UserSerializer


class RegistrationAPIView(APIView):

    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data)
