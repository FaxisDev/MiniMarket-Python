from django.shortcuts import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

class LogoutAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(reverse('admin:index')):
            if request.user.is_authenticated and not request.user.is_staff:
                # Cerrar sesión del usuario
                logout(request)

        return self.get_response(request)
