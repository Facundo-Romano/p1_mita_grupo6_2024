from datetime import datetime
from src.misc.metodos_os import obtener_ruta
from src.misc.metodos_uuid import generar_uuid
from src.misc.metodos_visualizacion import limpiar_consola, mostrar_equipos
from src.misc.metodos_validacion import validar_texto, validar_contraseña, validar_mail
from src.tablas.equipo.metodos_equipo import obtener_equipos

RUTA_USUARIOS = obtener_ruta('usuarios.txt')

def menu_login():
    limpiar_consola()

    while True:
        print('\n\n\nMenú login')
        print('1. Iniciar sesión')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('\nElija una opción: ')

        if opcion == '1':
            return login()
        elif opcion == '2':
            registrar()
        elif opcion == '3':
            break
        else:
            print('\nOpción no válida')

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
    #PENDIENTE: Agregar try except
    #PENDIENTE: Agregar salto de linea 
    # Solicitar los datos al usuario
    (nombre, apellido, mail, contraseña, uuid_equipo) = obtener_datos_usuario()

    # Generar un UUID para el nuevo usuario
    nuevo_uuid = str(generar_uuid())
    
    # Obtener la fecha actual para 'created_at'
    created_at = datetime.now().strftime("%d-%m-%Y")
    
    # 'deleted_at' se establece como None por defecto
    deleted_at = None
    
    # Crear el diccionario del nuevo usuario
    nuevo_usuario = {
        "uuid": nuevo_uuid,
        "nombre": nombre,
        "apellido": apellido,
        "mail": mail,
        "contraseña": contraseña,
        "uuid_equipo": uuid_equipo,
        "created_at": created_at,
        "deleted_at": deleted_at
    }
    
    # Guardar el usuario en el archivo txt
    with open(RUTA_USUARIOS, 'a', encoding='UTF-8') as archivo:
        archivo.write(f"{nuevo_usuario['uuid']};{nuevo_usuario['nombre']};{nuevo_usuario['apellido']};"
                      f"{nuevo_usuario['mail']};{nuevo_usuario['contraseña']};{nuevo_usuario['uuid_equipo']};"
                      f"{nuevo_usuario['created_at']};{nuevo_usuario['deleted_at']}")

    print("\nUsuario registrado exitosamente.")
    return nuevo_usuario

def obtener_datos_usuario():
    nombre = input("\nIngrese nombre: ")

    while (not validar_texto(nombre, "nombre")):
        nombre = input("\nIngrese nombre: ")

    apellido = input("\nIngrese apellido: ")

    while (not validar_texto(apellido, "apellido")):
        apellido = input("\nIngrese apellido: ")

    mail = input("\nIngrese mail: ")

    while (not validar_mail(mail)):
        mail = input("\nIngrese mail: ")
        
    contraseña = input("\nIngrese contraseña: ")

    while (not validar_contraseña(contraseña)):
        contraseña = input("\nIngrese contraseña: ")

    #Logica de eleccion de equipo
    print("\nSeleccione un equipo para su usuario: ")
    equipos = obtener_equipos()
    mostrar_equipos(equipos)
    equipo_seleccionado = elegir_equipo(equipos)

    return (
        nombre,
        apellido,
        mail,
        contraseña,
        equipo_seleccionado
    )

def elegir_equipo(equipos):
    while True:
        try:
            numero = int(input("\nElige el número del equipo: "))
            if 1 <= numero <= len(equipos):
                equipo_seleccionado = equipos[numero - 1]
                print(f"\nHas seleccionado: {equipo_seleccionado['nombre']}")
                return equipo_seleccionado['uuid']
            else:
                print("\nNúmero no válido. Intenta nuevamente.")
        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa un número.")