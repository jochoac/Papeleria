"""Papeleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import Papeleria.views as v
import Datos.views as dv

# Rutas para navegar en el sistema
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',dv.loginP , name= 'login'),
    path('logout/',dv.logoutP, name= 'logout'),
    path('productos/', v.productos, name= 'productos'),
    path('consulta/', v.consulta, name= 'consulta'),
    path('gesnom/', dv.gesnom, name= 'gesnom'),
    path('gesnom/<str:codigo>', dv.actualizarN, name= 'actualizarN'),
    path('Recibirpedido/', v.recibped, name= 'recibped'),
    path('registrarproducto/', dv.regispro, name= 'regispro'),
    path('registrarproducto/<str:codigo>', dv.actualizarP, name= 'actualizarP'),
    path('actualizarempleado/<str:codigo>', v.actempl, name = 'actempl'),
    path('actualizarproducto/<str:codigo>', v.actpro, name = 'actpro'),
    path('actualizarproveedor/<str:codigo>', v.actprov, name = 'actprov'),
    path('actualizarnomina/<str:codigo>', v.actgesnom, name ='actgesnom'),
    path('registrarnomina/', dv.regnom, name= 'regnom'),
    path('registrarproveedores/', dv.regprov, name= 'regprov'),
    path('cart/<str:categoria>',dv.cart, name= 'cart'),
    path('cart/',dv.cart, name= 'cart'),
    path('endventa/',dv.end_venta, name= 'endventa'),
    #path('base/', v.base),
    path('checkout/', v.checkout),
]
