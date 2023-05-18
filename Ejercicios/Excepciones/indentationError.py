def imprimir_datos(nombre, edad):
    try:
        print("Nombre:", nombre)
        print("Edad:", edad)
        print("¡Fin de la función!")
    except Exception as e:
        print("Ocurrió un error:", e)

imprimir_datos("John Doe", 25)

#La línea debería tener una indentación menor para estar al mismo nivel que las otras líneas de código dentro de la función