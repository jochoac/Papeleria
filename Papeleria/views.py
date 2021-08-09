from Datos.models import Empleado, Pedido, Producto, Proveedor, Nomina, Venta, Pedido, DetalleVenta
from django.shortcuts import render
from Datos.views import checkLG
  
# Funcion para cargar la página principal
def productos(request):
    empleados = Empleado.objects.all()
    for empleado in empleados:
        if empleado.logged == True:
            return render(request, 'Productos.html', {'user': empleado})
    return render(request, 'login.html')

# Funcion para cargar la página de consultas
def consultas(request):
    if checkLG():
        return render(request, 'Consultas.html')

    return render(request, 'login.html')

# Funcion para ir a la página de recibir pedidos
def recibped(request):
    if checkLG():
        proveedores= Proveedor.objects.all()
        productos= Producto.objects.all()
        return render(request,'RecibPed.html',{'proveedores':proveedores, 'productos':productos}) 
    return render(request, 'login.html')

# Funcion para ir al formulario de actualizar productos
def actpro(request,codigo):
    if checkLG():
        producto = Producto.objects.get(Codigo=codigo)
        return render(request, 'Actpro.html', {'producto': producto})
    return render(request, 'login.html')

# Funcion para ir al formulario de actualizar nóminas
def actgesnom(request, codigo):
    if checkLG():
        nomina = Nomina.objects.get(codigo=codigo)
        empleados = Empleado.objects.all()
        return render( request, 'actgesnom.html', {'nomina': nomina, 'empleados': empleados})
    return render(request, 'login.html')

# Funcion para ir al formulario de actualizar empleados
def actempl(request,codigo):
    if checkLG():
        empleado = Empleado.objects.get(DNI=codigo)
        return render(request, 'Actempl.html', {'empleado': empleado})
    
    return render(request, 'login.html')

# Funcion para ir al formulario de actualizar proveedores
def actprov (request, codigo):
    if checkLG(): 
        proveedor = Proveedor.objects.get(NIT=codigo)
        print(proveedor.Nombre)
        return render(request, 'actprov.html', {'proveedor': proveedor })

    return render(request, 'login.html' )

# Funcion para ir al carrito
def checkout (request):
    return render(request, 'Checkout.html')

# Funcion para cargar las consultas
def consulta (request):
    categoria = request.POST.get('comboc', 'Productos')
    if checkLG():
        if categoria == 'Productos':
            retorno = Producto.objects.all()
            headers = Producto.getColumns()
        elif categoria == 'Proveedores':
            retorno = Proveedor.objects.all()
            headers = Proveedor.getColumns()
        elif categoria == 'Nomina':
            retorno = Empleado.objects.all()
            headers = Empleado.getColumns()
        elif categoria == 'Ventas':
            retorno = Venta.objects.all()
            headers = Venta.getColumns()
        elif categoria == 'Pedidos':
            retorno = Pedido.objects.all()
            headers = Pedido.getColumns()
        else:
            retorno = Producto.objects.all()
            headers = Producto.getColumns()
        
        return render(request, 'Consultas.html', {'headers':headers, 'retorno':retorno, 'categoria': categoria})
    return render(request,'login.html')  

def detalleV(request,codigo):
    if checkLG():
        venta = Venta.objects.get(id=codigo)
        detalles = DetalleVenta.objects.filter(Venta=venta)
        print(detalles)
        return render(request, 'detalleVenta.html', {'venta': venta, 'detalles': detalles})
    return render(request, 'login.html')


