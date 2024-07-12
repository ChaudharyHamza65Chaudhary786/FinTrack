from rest_framework_simplejwt.tokens import RefreshToken

from . models import User


class UserHelper:
    def get_refresh_token(self, user_name):
        user = User.objects.get(username=user_name)
        refresh = RefreshToken.for_user(user)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
