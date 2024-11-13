from misc.metodos_visualizacion import limpiar_consola
from modulos.login.modulo_login import menu_login
from modulos.tareas.modulo_tareas import menu_tareas
from modulos.proyectos.modulo_proyecto import menu_proyectos
from modulos.equipos.modulo_equipos import menu_equipos
from modulos.proyectos.modulo_proyecto import menu_proyectos
from misc.metodos_visualizacion import mostrar_usuario_matriz

def menu_principal():
    limpiar_consola()
    usuario = menu_login()

    if not usuario:
        print('Adios.\n')
        return
    
    while True:
        limpiar_consola()
        print("\nBienvenido: \n")
        mostrar_usuario_matriz(usuario)
        print('\nMenú principal')
        print('1. Equipos')
        print('2. Proyectos')
        print('3. Tareas')
        print('4. Salir')

        opcion = input('\nSeleccione una opción: ')

        if opcion == '1':
            menu_equipos(usuario)
        elif opcion == '2':
            
            menu_proyectos(usuario)
        elif opcion == '3':
            
            menu_tareas(usuario)
        elif opcion == '4':
            break
        else:
            print('Opción inválida')