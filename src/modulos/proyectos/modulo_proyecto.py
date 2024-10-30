from misc.metodos_validacion import validar_texto, validar_fecha
from misc.metodos_visualizacion import limpiar_consola, mostrar_proyectos
from tablas.proyecto.metodos_proyecto import crear_proyecto, obtener_proyectos


def menu_proyectos(usuario):
    limpiar_consola()
    while True:
        print("Menú de proyectos")
        print("1. Mis proyectos")
        print("2. Crear nuevo proyecto")
        print("3. Editar proyecto")
        print("4. Eliminar proyecto")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Proyectos: ")
            # Llamar a la función para obtener todos los proyectos
            proyectos = obtener_proyectos()
            mostrar_proyectos(proyectos)
        elif opcion == "2":
            # Llamar a la función para crear tarea
            [nombre_proyecto, end_date] = obtener_datos_proyecto(usuario)

            crear_proyecto(nombre_proyecto, end_date)
        elif opcion == "3":
            # Llamar a la función para modificar tarea
           """  tareas = obtener_tareas(usuario)
            mostrar_tareas(tareas)
            numero = input("Ingrese el numero de la tarea a modificar: ")

            tarea_a_modificar = tareas[numero]

            print(tarea_a_modificar)

            [titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date] = obtener_datos_tarea(usuario)

            modificar_tarea(tarea_a_modificar['uuid'], titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, tarea_a_modificar['created_at'], end_date) """
        elif opcion == "4":
            # Llamar a la función para eliminar tarea
            """ tareas = obtener_tareas(usuario)
            
            mostrar_tareas(tareas)
            
            numero = input("Ingrese el numero de la tarea a modificar: ")

            tarea_a_eliminar = tareas[numero]

            print('Se va a eliminar la tarea: ')
            print(tarea_a_eliminar)
            confirmacion = input('¿Está seguro que desea eliminar la tarea? (s/n)')

            if confirmacion == 's':
                eliminar_tarea(tarea_a_eliminar['uuid']) """
        elif opcion == "5":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_proyecto(usuario):

    # Ver que pedir con Usuario
    """
    Obtiene los datos necesarios para crear un proyecto.
    Retorna una lista con los elementos introducidos.
    """

    nombre_proyecto = input("Ingresar nombre del proyecto: ")

    while (not validar_texto(nombre_proyecto, "nombre")):
        nombre_proyecto = input("Ingresar nombre del proyecto: ")
    
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    return [nombre_proyecto, end_date]