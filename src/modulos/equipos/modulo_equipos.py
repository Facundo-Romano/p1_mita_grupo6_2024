from misc.metodos_visualizacion import limpiar_consola

def menu_equipos(usuario):
    while True:
        """ limpiar_consola()
        print("Menú de tareas")
        print("1. Mis tareas")
        print("2. Crear nueva tarea")
        print("2. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Tareas: ")
            # Llamar a la función para obtener tarea
            tareas = obtener_tareas(usuario)
            mostrar_tareas(tareas)
        elif opcion == "2":
            # Llamar a la función para crear tarea
            [titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date] = obtener_datos_tarea(usuario)
            
            crear_tarea(titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date)
        elif opcion == "3":
            # Llamar a la función para modificar tarea
            tareas = obtener_tareas(usuario)
            mostrar_tareas(tareas)
            numero = input("Ingrese el numero de la tarea a modificar: ")

            tarea_a_modificar = tareas[numero]

            print(tarea_a_modificar)

            [titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date] = obtener_datos_tarea(usuario)

            modificar_tarea(tarea_a_modificar['uuid'], titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, tarea_a_modificar['created_at'], end_date)
        elif opcion == "4":
            # Llamar a la función para eliminar tarea
            tareas = obtener_tareas(usuario)
            
            mostrar_tareas(tareas)
            
            numero = input("Ingrese el numero de la tarea a modificar: ")

            tarea_a_eliminar = tareas[numero]

            print('Se va a eliminar la tarea: ')
            print(tarea_a_eliminar)
            confirmacion = input('¿Está seguro que desea eliminar la tarea? (s/n)')

            if confirmacion == 's':
                eliminar_tarea(tarea_a_eliminar['uuid'])
        elif opcion == "5":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.") """

menu_equipos()