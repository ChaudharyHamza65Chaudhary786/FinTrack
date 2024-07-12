from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializer import UserSerializer


@api_view(['POST'])
def register(request):
    response = None

    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = Response(serializer.validated_data)
    return response
