from misc.metodos_os import obtener_ruta
from datetime import datetime
from misc.metodos_uuid import generar_uuid
from misc.metodos_visualizacion import limpiar_consola
from misc.metodos_validacion import validar_texto, validar_contraseña, validar_mail

RUTA_USUARIOS = obtener_ruta('usuarios.txt')

def menu_login():
    limpiar_consola()
    print('Menú login')

    while True:
        print('1. Iniciar sesión')
        print('2. Registrarse')
        print('3. Salir')
        print('4. Saltear login')
        opcion = input('Elija una opción: ')

        if opcion == '1':
            return login()
        elif opcion == '2':
            registrar()
        elif opcion == '3':
            break
        elif opcion == '4':
            return {
                "uuid": "1",
                "nombre": "Usuario",
                "apellido": "De Prueba",
                "mail": "asd@asd.com",
                "contraseña": "123456",
                "uuid_equipo": "1",
                "created_at": "2021-09-01 00:00:00",
                "deleted_at": None
            }
        else:
            print('Opción no válida')


def login():
    try:
        archivo_usuarios = open(RUTA_USUARIOS, 'r', encoding='UTF-8')

        mail = input('Ingrese su mail: ')

        contraseña = input('Ingrese su contraseña: ')

        linea = archivo_usuarios.readline()

        while linea:
            usuario = linea.strip().split(';')

            if mail == usuario[3] and contraseña == usuario[4]:
                return {
                    "uuid": usuario[0],
                    "nombre": usuario[1],
                    "apellido": usuario[2],
                    "mail": usuario[3],
                    "contraseña": usuario[4],
                    "uuid_equipo": usuario[5],
                    "created_at": usuario[6],
                    "deleted_at": usuario[7]
                }
            
            linea = archivo_usuarios.readline()

        raise Exception('Usuario no encontrado')

 
    except Exception as e:
        print(e)
        return False

    finally:
        archivo_usuarios.close()
    

def registrar():
    directorio_actual = os.getcwd()
    ruta_absoluta = os.path.join(directorio_actual, 'assets', 'usuarios.txt')

    archivo_usuarios = open(ruta_absoluta, 'a', encoding='UTF-8')

    datos_usuario = obtener_datos_usuario()

    #pendiente terminar



def obtener_datos_usuario():
    nombre = input("Ingrese nombre: ")

    while (not validar_texto(nombre, "nombre")):
        nombre = input("Ingrese nombre: ")

    apellido = input("Ingrese apellido: ")

    while (not validar_texto(apellido, "apellido")):
        apellido = input("Ingrese apellido: ")

    mail = input("Ingrese mail: ")

    while (not validar_mail(mail)):
        mail = input("Ingrese mail: ")
        
    contraseña = input("Ingrese contraseña: ")

    while (not validar_contraseña(contraseña)):
        contraseña = input("Ingrese contraseña: ")

    #Logica de eleccion de equipo


    return [
        generar_uuid(),
        nombre,
        apellido,
        mail,
        contraseña,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        None,
    ]