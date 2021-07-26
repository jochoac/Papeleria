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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', v.login, name= 'login'),
    path('productos/', v.productos, name= 'productos'),
    path('consultas/', v.consultas, name= 'consultas'),
    path('gesnom/', v.gesnom, name= 'gesnom'),
    path('nomina/', v.nomina, name= 'nomina'),
    path('proveedores/', v.proveedores, name= 'proveedores'),
    path('Recibirpedido/', v.recibped, name= 'recibped'),
    path('registrarproducto/', v.regispro, name= 'regispro'),
    path('registrarproducto/<str:codigo>', v.actualizarP, name= 'actualizarP'),
    path('actualizarempleado/<str:codigo>', v.actempl, name = 'actempl'),
    path('actualizarproducto/<str:codigo>', v.actpro, name = 'actpro'),
    path('registrarnomina/', v.regnom, name= 'regnom'),
    path('registrarproveedores/', v.regprov, name= 'regprov'),
    path('vender/', v.vender, name= 'vender'),
    path('base/', v.base),  
]
