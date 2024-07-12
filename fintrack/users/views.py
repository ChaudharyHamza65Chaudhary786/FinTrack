from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . serializer import UserSerializer, LoginSerializer
from . helper import UserHelper


@api_view(['POST'])
def register(request):
    response = None

    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    response = Response(serializer.validated_data)
    return response


@api_view(['POST'])
def login(request):
    user_helper = UserHelper()

    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    response = user_helper.get_refresh_token(serializer.validated_data["username"])
    return Response(response)
