from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializer import UserSerializer


@api_view(['POST'])
def register(request):
    response = None

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = Response(serializer.validated_data)
    else:
        response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return response
