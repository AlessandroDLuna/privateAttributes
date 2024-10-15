from classVenta import Venta

# Crear una instancia de Venta
venta = Venta(id_venta=1, fecha="15/10/2024", cliente="Alejandro")

# Solicitar al usuario que ingrese los datos de los productos
for producto in ["Producto A", "Producto B", "Producto C"]:
    venta.ingresar_producto(producto)

# Mostrar los detalles de la venta
print(venta)
