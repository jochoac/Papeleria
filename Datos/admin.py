from django.contrib import admin
import Datos.models as mds

# Register your models here.
admin.site.register(mds.Producto)
admin.site.register(mds.Empleado)
admin.site.register(mds.Cliente)
admin.site.register(mds.Venta)
admin.site.register(mds.DetallePedido)
admin.site.register(mds.Pedido)
admin.site.register(mds.Proveedor)
admin.site.register(mds.DetalleVenta)

