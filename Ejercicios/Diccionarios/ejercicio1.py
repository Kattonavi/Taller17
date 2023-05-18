# Creamos un diccionario para almacenar el inventario de productos
inventarioProductos = {
    "unidadArroz": 10,
    "unidadHuevo": 5,
    "unidadPapa": 3,
    "unidadCebolla": 8
}

# Actualizamos el inventario de un producto
producto = "unidadArroz"
cantidad = 2
inventarioProductos[producto] -= cantidad

# Mostramos el inventario actualizado del producto
print(f"El inventario de {producto} es ahora {inventarioProductos[producto]}")
