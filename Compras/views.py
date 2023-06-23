from django.shortcuts import render
from Login.decorators import empleados_login_required

# Create your views here.
@empleados_login_required
def compras_view(request):
    if request.method == 'GET':
       
    # Lógica de la vista del panel de control o dashboard
        return render(request, 'create_compras.html')

