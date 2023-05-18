inventario_frutas = {
    "manzana": 10,
    "naranja": 5,
    "plátano": 8,
    "uva": 15
}

fruta = input("Ingresa el nombre de una fruta: ")

if fruta in inventario_frutas:
    cantidad = inventario_frutas[fruta]
    print("La cantidad disponible de", fruta, "es:", cantidad)
else:
    print("La fruta", fruta, "no está disponible en el inventario.")
