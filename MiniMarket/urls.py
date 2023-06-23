"""MiniMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Compras.views import compras_view

from Ventas.views import agregar_carrito, crear_venta, vaciar_carrito, descuento_carrito, guardar_venta
from .admin import admin_site
from Login.views import login_view, dashboard, logout_view

urlpatterns = [
    path('', dashboard, name='inicio'),
    path('admin/', admin_site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('crear/venta', crear_venta, name='crear_venta'),
    path('guardar/venta', guardar_venta, name='guardar_venta'),
    path('carrito/agregar', agregar_carrito, name='agregar_carrito'),
    path('carrito/vaciar', vaciar_carrito, name='vaciar_carrito'),
    path('carrito/descuento', descuento_carrito, name='descuento_carrito'),

    path('crear/compra', compras_view, name='compras_view'),

]
