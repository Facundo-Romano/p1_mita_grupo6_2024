from misc.metodos_visualizacion import limpiar_consola

def menu_login():
    limpiar_consola()
    print('menu login')

    while True:
        print('1. Iniciar sesión')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('Elija una opción: ')

        if opcion == '1':
            login()
        elif opcion == '2':
            registrar()
        elif opcion == '3':
            break
        else:
            print('Opción no válida')


def login():
    try:
        archivo_usuarios = open(r'd:/usuarios.txt', 'r', encoding='UTF-8')

        mail = input('Ingrese su mail: ')

        contraseña = input('Ingrese su contraseña: ')

        linea = archivo_usuarios.readline()

        while linea:
            usuario = linea.strip().split(';')

            if mail == usuario[3] and contraseña == usuario[4]:
                return usuario
            
            linea = archivo_usuarios.readline()

        raise Exception('Usuario no encontrado')

 
    except Exception as e:
        print(e)
        return False

    finally:
        archivo_usuarios.close()
    

def registrar():
    return

