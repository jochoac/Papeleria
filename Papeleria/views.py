from django import http
from django.http import HttpResponse
from Datos.models import Empleado, Producto, Proveedor
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

#Temp
def base(request):
    return render(request, 'Base.html')

def productos(request):
    return render(request, 'Productos.html')

def consultas(request):
    return render(request, 'Consultas.html')

def gesnom(request):
    return render(request, 'Gesnom.html')

def nomina(request):
    return render(request, 'Nomina.html')

def proveedores(request):
    return render(request, 'Proveedores.html')

def recibped(request):
    return render(request,'RecibPed.html')

def regispro(request): 

    if request.method == 'POST':
        pro = Producto(
            Codigo = request.POST['codigo'],
            Nombre = request.POST['nombre'],
            Referencia = request.POST['ref'],
            Categoria = request.POST['cat'],
            Precio = request.POST['price'],
            Existencia = request.POST['cant'])
        pro.save()

    productos = Producto.objects.all()
    return render(request, 'Regispro.html', {'productos': productos})

def regnom(request):

    if request.method == 'POST':
        emp = Empleado(
            DNI=request.POST['id'],
            Nombre=request.POST['nombre'],
            Apellido=request.POST['apellido'],
            Cargo=request.POST['cargo'],
            Estado=request.POST['estado'])
        emp.save()

    empleados = Empleado.objects.all()
    return render(request, 'Regnom.html', {'empleados': empleados})

def regprov(request): 
    return render(request, 'Regprov.html')

def vender(request):
    return render(request, 'Vender.html')

def actpro(request,codigo):
    producto = Producto.objects.get(Codigo=codigo)
    return render(request, 'Actpro.html', {'producto': producto})

def actempl(request,codigo):
    empleado = Empleado.objects.get(DNI=codigo)
    return render(request, 'Actempl.html', {'empleado': empleado})

def uptemple (request, codigo):
    emp = Empleado.objects.get(DNI=codigo)
    emp.Nombre = request.POST['nombre']
    emp.Apellido = request.POST['apellido']
    emp.Cargo = request.POST['cargo']
    emp.Estado = request.POST['estado']
    emp.save()
    empleados = Empleado.objects.all()
    return render(request, 'Regnom.html', {'empleados': empleados})

def regprov(request):

    if request.method == 'POST':
        pro = Proveedor(
            NIT = request.POST['nit'],
            Nombre = request.POST['nombre'],
            Telefono = request.POST['tel'],)
        pro.save()

    prov = Proveedor.objects.all()
    return render(request, 'Regprov.html',{'proveedores': prov})

def actualizarP(request, codigo):
    pro = Producto.objects.get(Codigo=codigo)
    pro.Nombre = request.POST['nombre']
    pro.Referencia = request.POST['ref']
    pro.Categoria = request.POST['cat']
    pro.Precio = request.POST['price']
    pro.Existencia = request.POST['cant']
    pro.save()
    productos = Producto.objects.all()
    return render(request, 'Regispro.html', {'productos': productos})