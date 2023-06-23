from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from Login.decorators import empleados_login_required
from .backends import CustomUserBackend

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        clave = request.POST['clave']
        
        user = CustomUserBackend().authenticate(request, email=email, password=clave)

        if user is not None:
            # Establecer el atributo 'backend' en el objeto 'User'
            user.backend = 'Login.backends.CustomUserBackend'
            login(request, user)
            
            # Cambia 'dashboard' por la URL a la que deseas redirigir al iniciar sesión correctamente
            return redirect('inicio')
        else:
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


@empleados_login_required
def dashboard(request):
    # Lógica de la vista del panel de control o dashboard
    return render(request, 'inicio.html')


def logout_view(request):
    logout(request)
    # Cambia 'login' por la URL de la página de inicio de sesión
    return redirect('login')
