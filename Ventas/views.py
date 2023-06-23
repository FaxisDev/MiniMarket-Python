from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from django.db import transaction
from django.db.models import Q

from Login.decorators import empleados_login_required
from Productos.models import Productos
from Ventas.models import Ventas
from Empleados.models import Empleados
from datetime import date

# Create your views here.


@empleados_login_required
def crear_venta(request):
    if request.method == 'GET':
        contexto = {}

        filtro_productos = request.GET.get('filtro_productos')
        # Cargar lista de productos
        lista_productos = ''
        if filtro_productos:  # Si se ingresa algun dato en el buscador, el modelo lo  buscara
            lista_productos = Productos.objects.filter(
                Q(nombre__icontains=filtro_productos) | Q(descripcion__icontains=filtro_productos))
        else:
            lista_productos = Productos.objects.all()[:10]

        # Si utilizamos los botones de agregar producto este surtira efecto
        lista_carrito = request.session.get('pila_productos', [])

        # obtenemos valor de descuento_carrito almacenado
        descuento_carrito = request.session.get('descuento_carrito', 0)
   
        # obtenemos valor de sub total almacenado del carrito
        subtotal_carrito = request.session.get('subtotal_carrito', 0)

        for item in lista_carrito:
            subtotal_carrito = subtotal_carrito + float(item['precio'])

        # Validacion de descuento cuando es mayor que el subtotal (lo resetea a $0)
        if float(descuento_carrito) > float(subtotal_carrito):
            # Se agrega el mensaje a contexto
            contexto['descuento_carrito_error'] = "Descuento no aplicable, supera el subtotal."
            descuento_carrito = 0
            request.session['descuento_carrito'] = descuento_carrito

        total_carrito = float(subtotal_carrito) - float(descuento_carrito)

        # Datos que pasaremos al template

        contexto['lista_productos'] = lista_productos
        contexto['lista_carrito'] = lista_carrito
        contexto['descuento_carrito'] = descuento_carrito
        contexto['subtotal_carrito'] = subtotal_carrito
        contexto['total_carrito'] = total_carrito

        request.session.save()

    # Lógica de la vista del panel de control o dashboard
        return render(request, 'create_ventas.html', contexto)

    else:  # Vista de POST
        agregar_carrito()


def agregar_carrito(request):
    # Obtén el ID del producto agregado

    producto_id = request.GET.get('producto_id')
    # Obtén el producto desde la base de datos
    producto = Productos.objects.get(id=producto_id)

    # Accede a la variable de sesión "pila_productos" o crea una nueva si no existe
    pila_productos = request.session.get('pila_productos', [])

    producto_serializado = {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        'stock': producto.stock,
        'id_departamento': producto.id_departamento.id,
        'id_marca': producto.id_marca.id
    }

    # Agrega el producto a la pila
    pila_productos.append(producto_serializado)

    # Actualiza la variable de sesión
    request.session['pila_productos'] = pila_productos

    return redirect('crear_venta')


def vaciar_carrito(request):
    # Vaciar carrito
    request.session['pila_productos'] = []
    return redirect('crear_venta')


def descuento_carrito(request):
    # Vaciar carrito
    request.session['descuento_carrito'] = request.GET.get('descuento')
    return redirect('crear_venta')


#@empleados_login_required
def guardar_venta(request):
    if request.method == 'POST':

        lista_carrito = request.POST.get('lista_carrito')
        
        descuento_carrito = float(request.POST.get('descuento_carrito').replace(',', '.'))
        subtotal_carrito = float(request.POST.get('subtotal_carrito').replace(',', '.'))
        total_carrito = float(request.POST.get('total_carrito').replace(',', '.'))


        id_empleado = get_object_or_404(Empleados, id=request.user.id) #Obtenemos objeto de tipo empleados (debe ser objecto y no un int)
        # Crear registro en Ventasla tabla Ventas
        Ventas.objects.create(descuento=descuento_carrito, subtotal=subtotal_carrito,
                              total=total_carrito, fecha_venta=date.today(), id_empleado=id_empleado)

        # Esto ayudara a llenar el modelo ventasXProducto
        """ for item in lista_carrito:
            subtotal_carrito = subtotal_carrito + float(item['precio']) """

        return render(request, 'save_venta.html')
    else:
        return redirect('crear_venta')
