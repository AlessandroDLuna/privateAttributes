class Venta:
    def __init__(self, id_venta=None, fecha=None, cliente=None):
        self.__id_venta = id_venta
        self.__fecha = fecha
        self.__cliente = cliente

        # Inicializa el diccionario con los 3 productos disponibles
        self.__productos = {
            "Producto A": {"producto": "Producto A", "cantidad": 0, "precio_unitario": 0.0},
            "Producto B": {"producto": "Producto B", "cantidad": 0, "precio_unitario": 0.0},
            "Producto C": {"producto": "Producto C", "cantidad": 0, "precio_unitario": 0.0}
        }
        self.__total = 0.0

    @property
    def id_venta(self):
        return self.__id_venta

    @id_venta.setter
    def id_venta(self, value):
        self.__id_venta = value

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    @property
    def total(self):
        return self.__total

    # Método para ingresar los datos del producto manualmente
    def ingresar_producto(self, nombre):
        if nombre not in self.__productos:
            raise ValueError("Solo se permiten Producto A, Producto B o Producto C")

        try:
            cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
            precio_unitario = float(input(f"Ingrese el precio unitario de {nombre}: "))
            if cantidad < 0 or precio_unitario < 0:
                raise ValueError("La cantidad y el precio unitario deben ser no negativos")
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")
            return  # Termina la función si hay un error

        # Actualizar el diccionario del producto
        self.__productos[nombre]["cantidad"] = cantidad
        self.__productos[nombre]["precio_unitario"] = precio_unitario
        self.__calcular_total()

    # Método privado para calcular el total
    def __calcular_total(self):
        self.__total = sum(
            p["cantidad"] * p["precio_unitario"] for p in self.__productos.values()
        )

    # Mostrar detalles de la venta
    def __str__(self):
        productos_str = "\n".join(
            f"{p['producto']}: {p['cantidad']} unidades a ${p['precio_unitario']} cada uno"
            for p in self.__productos.values()
        )
        return (f"ID Venta: {self.__id_venta}\n"
                f"Fecha: {self.__fecha}\n"
                f"Cliente: {self.__cliente}\n"
                f"Productos:\n{productos_str}\n"
                f"Total: ${self.__total:.2f}")
