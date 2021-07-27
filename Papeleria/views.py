from Datos.models import Empleado, Producto, Proveedor
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def loginP(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Empleado.objects.get(DNI=username, Password=password)
        
        except Empleado.DoesNotExist:
            user = None

        if user is not None:
            user.logged = True
            user.save()
            return render(request, 'Productos.html',{'user': user})
        else:
            # messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'login.html')
    return render(request, 'login.html')

#Temp
def base(request):
    productos = Producto.objects.all()
    return render(request, 'Search.html',{'productos': productos})

def productos(request):
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            return render(request, 'Productos.html', {'user': empleado})
    return render(request, 'login.html')

def logoutP(request):
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            empleado.logged = False
            empleado.save()
            return render(request, 'login.html')

def consultas(request):
    return render(request, 'Consultas.html')

def gesnom(request):
    empleados = Empleado.objects.all()
    return render(request, 'Gesnom.html', {'empleados': empleados})

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
            Password = request.POST['pass'],
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

def actprov (request, codigo):
    proveedor = Proveedor.objects.get(NIT=codigo)
    print(proveedor.Nombre)
    return render(request, 'actprov.html', {'proveedor': proveedor })

