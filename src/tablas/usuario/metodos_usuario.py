def obtener_usuarios():
    return 'usuarios'

def obtener_usuario(id_usuario):
    return 'usuario'

def crear_usuario():
    """
    Funcion para crear usuario usando diccionario, le ingresamos el nombre y la contrasena y 
    la funcion devuelve la lista usuario con su id, nombre, mail y contrasena
    """
    id_usuario = int(input("Ingrese id usuario: "))
    nombre_usuario = input("Ingresar nombre del usuario: ")
    mail_usuario = input("Ingresar mail del usuario: ")
    contrasena_usuario = input("Ingresar contraseña del usuario: ")
    
    #Diccionario usuario
    usuario = {
        "id": id_usuario,
        "nombre": nombre_usuario,
        "mail": mail_usuario,
        "contrasena": contrasena_usuario
    }
    return usuario

def modificar_usuario(usuario):
    """
    Función para modificar los datos de un usuario existente.
    Se puede modificar el nombre, mail y contraseña.
    """
    print(f"Datos actuales del usuario: {usuario}")
    opcion = input("¿Qué desea modificar? (nombre/mail/contrasena): ").lower()

    if opcion == "nombre":
        usuario["nombre"] = input("Ingresar nuevo nombre del usuario: ")
    elif opcion == "mail":
        usuario["mail"] = input("Ingresar nuevo mail del usuario: ")
    elif opcion == "contrasena":
        usuario["contrasena"] = input("Ingresar nueva contraseña del usuario: ")
    else:
        print("Opción no válida.")

    return usuario

def asignar_rol_usuario(id_usuario, id_rol):
    return 'success'

def asignar_equipo_usuario(id_usuario, id_equipo):
    return 'success'

def eliminar_usuario(id_usuario):  
    return 'success'