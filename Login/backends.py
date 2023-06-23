from django.contrib.auth.backends import ModelBackend
from Empleados.models import Empleados

class CustomUserBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return Empleados.objects.get(pk=user_id)
        except Empleados.DoesNotExist:
            return None

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Empleados.objects.get(email=email,is_admin=False)
            if user.check_password(password):
                
                return user
        except Empleados.DoesNotExist:
            return None
