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

def checkLG():
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            return True
    return False


#Temp
def base(request):
    productos = Producto.objects.all()
    return render(request, 'Search.html',{'productos': productos})

def productos(request):
    if checkLG():
        return render(request, 'Productos.html')
    return render(request, 'login.html')

def logoutP(request):
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            empleado.logged = False
            empleado.save()
            return render(request, 'login.html')

def consultas(request):
    if checkLG():
        empleados = Empleado.objects.all()
        for empleado in empleados:
            if empleado.logged == True:
                return render(request, 'Consultas.html')
        
    return render(request, 'login.html')

def gesnom(request):
    if checkLG():
        empleados = Empleado.objects.all()
        return render(request, 'Gesnom.html', {'empleados': empleados})
    return render(request, 'login.html')

def recibped(request):
    if checkLG():
        return render(request,'RecibPed.html')
    
    return render(request, 'login.html' )

def regispro(request): 
    if checkLG():
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
        
    return render(request, 'login.html' )

def regnom(request):
    if checkLG():
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

    return render(request, 'login.html' )

    

def regprov(request): 
    if checkLG():
        return render(request, 'Regprov.html') 

    return render(request, 'login.html' )

def vender(request):
    if checkLG():
        return render(request, 'Vender.html')

    return render(request, 'login.html')

def actpro(request,codigo):
    if checkLG():
        producto = Producto.objects.get(Codigo=codigo)
        return render(request, 'Actpro.html', {'producto': producto})

    return render(request, 'login.html' )

def actempl(request,codigo):
    if checkLG():
        empleado = Empleado.objects.get(DNI=codigo)
        return render(request, 'Actempl.html', {'empleado': empleado})
    
    return render(request, 'login.html')

def regprov(request):
    if checkLG():
        if request.method == 'POST':
            pro = Proveedor(
                NIT = request.POST['nit'],
                Nombre = request.POST['nombre'],
                Telefono = request.POST['tel'],)
            pro.save()

        prov = Proveedor.objects.all()
        return render(request, 'Regprov.html',{'proveedores': prov})

    return render(request, 'login.html' )

def actualizarP(request, codigo):
    if checkLG():
        pro = Producto.objects.get(Codigo=codigo)
        pro.Nombre = request.POST['nombre']
        pro.Referencia = request.POST['ref']
        pro.Categoria = request.POST['cat']
        pro.Precio = request.POST['price']
        pro.Existencia = request.POST['cant']
        pro.save()
        productos = Producto.objects.all()
        return render(request, 'Regispro.html', {'productos': productos})

    return render(request, 'login.html' )

def actprov (request, codigo):
    if checkLG(): 
        proveedor = Proveedor.objects.get(NIT=codigo)
        print(proveedor.Nombre)
        return render(request, 'actprov.html', {'proveedor': proveedor })

    return render(request, 'login.html' )


def checkout (request):
    return render(request, 'Checkout.html')

