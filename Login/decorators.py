from django.shortcuts import HttpResponse
from django.shortcuts import redirect

def empleados_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        #return HttpResponse('is_staff'+str(request.user.is_staff)+' is auth'+str(request.user.is_authenticated))
        if not request.user.is_authenticated or request.user.is_staff: #Valida si esta autenticado #Valida si su usuario es de tipo empleado (debe ser False)
                # Personaliza el comportamiento cuando el usuario no está autenticado
                return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper
