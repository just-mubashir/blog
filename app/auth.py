from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuth(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None: return None
        try: User.objects.get(username=username)
        except User.DoesNotExist as e: raise AuthenticationFailed('No User Found') from e
        return (User, None)