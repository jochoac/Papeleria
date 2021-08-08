from django.shortcuts import render
from Datos.models import Empleado, Producto, Nomina, Proveedor

# Create your views here.

# Función para verificar si hay algun usuario con sesión activa 
def checkLG():
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            return True
    return False


# Función para inicio de sesión
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

# Funcion para cerrar sesión
def logoutP(request):
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            empleado.logged = False
            empleado.save()
            return render(request, 'login.html')

# Funcion para registrar una nómina
def gesnom(request):
    if checkLG():
        if request.method == 'POST':
            emp = Nomina(
                empleado = Empleado.objects.get(DNI=request.POST['empleado']),
                fechaInicio = request.POST['fechaI'],
                fechaFin = request.POST['fechaF'],
                costoHoras = request.POST['salariohora'],
                horas = request.POST['horaslaboradas'],
                horasDominicales = request.POST['horasdominicales'],
                horasExtra = request.POST['horasextras'],
                salario = request.POST['salariototal']
                )
            emp.save() # INSERT INTO Nomina VALUES (...)
        nominas = Nomina.objects.all() # SELECT * FROM Nomina
        empleados = Empleado.objects.all() # SELECT * FROM Empleado
        return render(request, 'Gesnom.html', {'nominas': nominas, 'empleados': empleados})
    return render(request, 'login.html')

# Funcion para registrar un producto
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
            pro.save() # INSERT INTO Producto VALUES (...)
        productos = Producto.objects.all() # SELECT * FROM Producto
        return render(request, 'Regispro.html', {'productos': productos})
    return render(request, 'login.html' )

# Funcion para registrar un empleado
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
            emp.save() # INSERT INTO Empleado VALUES (...)
        empleados = Empleado.objects.all() # SELECT * FROM Empleado
        return render(request, 'Regnom.html', {'empleados': empleados})
    return render(request, 'login.html' )

#Funcion para registrar un proveedor
def regprov(request):
    if checkLG():
        if request.method == 'POST':
            pro = Proveedor(
                NIT = request.POST['nit'],
                Nombre = request.POST['nombre'],
                Telefono = request.POST['tel'],)
            pro.save() # INSERT INTO Proveedor VALUES (...)

        prov = Proveedor.objects.all() # SELECT * FROM Proveedores
        return render(request, 'Regprov.html',{'proveedores': prov})

    return render(request, 'login.html' )

# Funcion para añadir cosas al carrito
def cart(request, categoria=None):
    if checkLG():
        if categoria is None:
            productos = Producto.objects.all() # SELECT * FROM Producto
            return render(request, 'Search.html',{'productos': productos})
        else:
            productos = Producto.objects.filter(Categoria=categoria) # SELECT * FROM producto WHERE Categoria = categoria
            return render(request, 'Search.html',{'productos': productos})
    return render(request, 'login.html')

# Funcion para actualizar un producto
def actualizarP(request, codigo):
    if checkLG():
        pro = Producto.objects.get(Codigo=codigo)
        pro.Nombre = request.POST['nombre']
        pro.Referencia = request.POST['ref']
        pro.Categoria = request.POST['cat']
        pro.Precio = request.POST['price']
        pro.Existencia = request.POST['cant']
        pro.save() # UPDATE Producto SET Nombre=nombre, ... WHERE Codigo = codigo
        productos = Producto.objects.all() # SELECT * FROM Producto
        return render(request, 'Regispro.html', {'productos': productos})

    return render(request, 'login.html')

def end_venta(request):
    if checkLG():
        print(request.POST)
        total = request.POST['total']
        # tabla = request.POST['codigo']
        print(total)
        sesion = Empleado.objects.get(logged=True)
        # venta = Venta(Empleado = sesion, Total=total)
        # venta.save()
        return render(request, 'Checkout.html')
    return render(request, 'login.html')


# Función para actualizar nómina
def actualizarN(request, codigo):
    if checkLG():
        nom = Nomina.objects.get(codigo=codigo)
        nom.fechaInicio = request.POST['fechaI']
        nom.fechaFin = request.POST['fechaF']
        nom.costoHoras = request.POST['salariohora']
        nom.horas = request.POST['horaslaboradas']
        nom.horasDominicales = request.POST['horasdominicales']
        nom.horasExtra = request.POST['horasextras']
        nom.salario = request.POST['salariototal']
        nom.save() # UPDATE Nomina SET, ... WHERE Codigo = codigo
        nominas = Nomina.objects.all() # SELECT * FROM Nomina
        empleados = Empleado.objects.all() # SELECT * FROM Empleados
        return render(request, 'Gesnom.html', {'nominas': nominas, 'empleados': empleados})
    return render(request, 'login.html')