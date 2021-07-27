from django.db import models

# Create your models here.
#Table Producto
class Producto(models.Model):
    Codigo = models.CharField(max_length=20, primary_key=True)
    Nombre = models.CharField(max_length=50)
    Referencia = models.CharField(max_length=50)
    Categoria = models.CharField(max_length=50)
    Precio = models.DecimalField(max_digits=10, decimal_places=2)
    Existencia = models.IntegerField()


    def __str__(self):
        return self.Codigo + '%' + self.Nombre + '%' + self.Referencia + '%' + self.Categoria + '%' + str(self.Precio) + '%' + str(self.Existencia)

# Table Empleado
class Empleado(models.Model):
    DNI = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Cargo = models.CharField(max_length=100)
    Estado = models.CharField(max_length=10)
    Password = models.CharField(max_length=100, default='1234')
    logged = models.BooleanField(default=False)


# Table Proveedor
class Proveedor(models.Model):
    NIT = models.CharField(primary_key=True, max_length=20)
    Nombre = models.CharField(max_length=100)
    Telefono = models.IntegerField()

# Table Pedido
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now_add=True)
    Hora = models.TimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

# Table Venta
class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now_add=True)
    Total = models.DecimalField(max_digits=10, decimal_places=2)

# Table DetallePedido
class DetallePedido(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    Cantidad = models.IntegerField()

# Table DetalleVenta
class DetalleVenta(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    Cantidad = models.IntegerField()

class Nomina(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    costoHoras = models.DecimalField(max_digits=10, decimal_places=2)
    horas = models.IntegerField()
    horasDominicales = models.IntegerField()
    horasExtra = models.IntegerField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

