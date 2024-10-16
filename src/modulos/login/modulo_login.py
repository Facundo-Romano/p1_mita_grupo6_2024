def login_menu():
    print('login')

    while True:
        print('1. Iniciar sesión')
        print('2. Registrarse')
        print('3. Salir')
        opcion = input('Elija una opción: ')

        if opcion == '1':
            print('Iniciar sesión')
        elif opcion == '2':
            print('Registrarse')
        elif opcion == '3':
            break
        else:
            print('Opción no válida')

