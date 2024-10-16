from tablas.tarea.metodos_tarea import crear_tarea, modificar_tarea, obtener_tareas, eliminar_tarea
from misc.metodos_visualizacion import mostrar_tareas
from tablas.proyecto.metodos_proyecto import  modificar_proyecto



def menu_principal():
    while True:
        print()
        print("Menú principal")
        print("1. Crear tarea")
        print("2. Modificar tarea")
        print("3. Mostrar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Llamar a la función para crear tarea
            crear_tarea()
        elif opcion == "2":
            # Llamar a la función para modificar tarea
            uuid = input("Ingrese el uuid de la tarea a modificar: ")
            modificar_tarea(uuid)
        elif opcion == "3":
            print("Tareas: ")
            # Llamar a la función para obtener tarea
            tareas = obtener_tareas()
            mostrar_tareas(tareas)
        elif opcion == "4":
            # Llamar a la función para eliminar tarea
            uuid = input("Ingrese el uuid de la tarea a eliminar: ")
            eliminar_tarea(uuid)
        elif opcion == "6":
            modificar_proyecto('test2')
        elif opcion == "5":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()