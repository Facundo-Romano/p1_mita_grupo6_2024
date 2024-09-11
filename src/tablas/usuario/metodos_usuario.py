from equipo.metodos_equipo import obtener_equipo
from misc.metodos_uuid import generar_uuid
import re
from datetime import datetime

def obtener_usuarios():
    return 'usuarios'

def obtener_usuario(id_usuario):
    return 'usuario'

def crear_usuario():
    """
    Funcion para crear usuario usando diccionario, le ingresamos el nombre y la contrasena y 
    la funcion devuelve la lista usuario con su id, nombre, apellido, equipo, mail y contrasena
    """
    id_usuario = generar_uuid()
    nombre_usuario = input("Ingresar nombre del usuario: ")
    apellido_usuario = input("Ingresar apellido del usuario: ")
    equipo_usuario = obtener_equipo()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mail_usuario = input("Ingresar mail del usuario: ")
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_regex, mail_usuario):
        print("Email no válido. Por favor, ingrese un email válido.")
    contrasena_usuario = input("Ingresar contraseña del usuario: ")
    


    equipo_usuario = None
    
    while equipo_usuario == None:
        print("Seleccione el equipo al que desea asignar al usuario: ")

        for equipo in obtener_equipo:
            print(f"equipo: {equipo['nombre']}")

        nombre_equipo = input("Ingrese el nombre del equipo: ")

        for equipo in obtener_equipo:
            if equipo['nombre'] == nombre_equipo:
                equipo_usuario = equipo
                break
        
        if equipo_usuario == None:
            print("Equipo no encontrado.")

    #Diccionario usuario
    usuario = {
        "id": id_usuario,
        "nombre": nombre_usuario,
        "apellido": apellido_usuario,
        "equipo" : equipo_usuario,
        "created_at": created_at,
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
    elif opcion == "apellido":
        usuario["apellido"] = input("Ingresar nuevo apellido del usuario: ")
    elif opcion == "equipo":
        usuario["equipo"] = input("Ingresar nuevo equipo del usuario: ")
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