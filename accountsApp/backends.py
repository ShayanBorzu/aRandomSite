from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=str, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
        except User.DoesNotExist:
            return None
        else:
            if password and user.check_password(password):
                return user
        return None
