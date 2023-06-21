from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, HttpResponse

from Empleados.models import Empleados

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        clave = request.POST['clave']
        
        empleados = Empleados.objects.get(email = email)
        if empleados.check_password(clave):
            
            login(request, empleados)
            # Cambia 'dashboard' por la URL a la que deseas redirigir al iniciar sesión correctamente
            return redirect('inicio')
        else:
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


##@login_required
def dashboard(request):
    # Lógica de la vista del panel de control o dashboard
    return render(request, 'inicio.html')


def logout_view(request):
    logout(request)
    # Cambia 'login' por la URL de la página de inicio de sesión
    return redirect('login')
