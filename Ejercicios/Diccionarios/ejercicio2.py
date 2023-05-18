# Creamos un diccionario para almacenar los datos de los usuarios
registroUsuarios = {}

# Solicitamos información del usuario
nombreUsuario = input("Ingrese su nombre: ")
edadUsuario = int(input("Ingrese su edad: "))
emailUsuario = input("Ingrese su correo electrónico: ")

# Guardamos los datos del usuario en el diccionario
registroUsuarios[nombreUsuario] = {
    "edad": edadUsuario,
    "email": emailUsuario
}

# Mostramos los datos almacenados
print(f"Registro exitoso. Datos del usuario: {registroUsuarios}")
