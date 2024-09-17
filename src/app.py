from tablas.tarea.metodos_tarea import crear_tarea, modificar_tarea, obtener_tareas, eliminar_tarea
from misc.metodos_visualizacion import mostrar_tareas

usuarios = [
    ['uuid', 'nombre', 'apellido', 'equipo', 'mail', 'contraseña', 'created_at'],
]

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
            modificar_tarea()
        elif opcion == "3":
            print()
            # Llamar a la función para obtener tarea
            tareas = obtener_tareas()
            mostrar_tareas(tareas)
        elif opcion == "4":
            # Llamar a la función para eliminar tarea
            eliminar_tarea()
        elif opcion == "5":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu_principal()