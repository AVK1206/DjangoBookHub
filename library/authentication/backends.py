from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class CustomUserBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        """
        Overridden method that give us ability to check is_superuser
        Args:
            request:
            email:
            password:
            **kwargs:

        Returns: user if password matched or None

        """
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None