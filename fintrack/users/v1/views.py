from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializer import UserSerializer


@api_view(['POST'])
def register(request):

    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.validated_data)
