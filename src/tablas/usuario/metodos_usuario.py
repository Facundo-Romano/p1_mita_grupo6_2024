from tablas.equipo.metodos_equipo import obtener_equipos
from misc.metodos_uuid import generar_uuid
from misc.metodos_validacion import validar_mail, validar_contraseña, validar_texto
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
    equipos = obtener_equipos()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    equipo_usuario = None

    nombre_usuario = input("Ingresar nombre del usuario: ")

    while (validar_texto(nombre_usuario, "nombre")):
        nombre_usuario = input("Ingresar nombre del usuario: ")

    apellido_usuario = input("Ingresar apellido del usuario: ")

    while (validar_texto(apellido_usuario, "apellido")):
        apellido_usuario = input("Ingresar apellido del usuario: ")
        
    mail_usuario = input("Ingresar mail del usuario: ")

    while (not validar_mail(mail_usuario)):
        mail_usuario = input("Ingresar mail del usuario: ")

    contraseña_usuario = input("Ingresar contraseña del usuario\n (La contraseña debe tener al menos 8 caracteres, una letra mayúscula, un número y un caracter especial):")
    
    while (not validar_contraseña(contraseña_usuario)):
        contraseña_usuario = input("Ingresar contraseña del usuario: ")
    
    print("Seleccione el equipo al que desea asignar al usuario: ")

    while not equipo_usuario:
        for equipo in equipos:
            print(f"Equipo: {equipo['nombre']}")

        nombre_equipo = input("Ingrese el nombre del equipo: ")

        for equipo in equipos:
            if equipo['nombre'] == nombre_equipo:
                equipo_usuario = equipo
                break
        
        if not equipo_usuario:
            print("Equipo no encontrado.")

    #Diccionario usuario
    usuario = {
        "id": id_usuario,
        "nombre": nombre_usuario,
        "apellido": apellido_usuario,
        "equipo" : equipo_usuario['uuid'],
        "mail": mail_usuario,
        "contraseña": contraseña_usuario,
        "created_at": created_at,
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