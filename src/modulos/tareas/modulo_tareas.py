from misc.metodos_validacion import validar_fecha, validar_texto
from misc.metodos_visualizacion import mostrar_tareas, limpiar_consola
from tablas.equipo.metodos_equipo import obtener_equipo_por_usuario
from tablas.proyecto.metodos_proyecto import obtener_proyectos
from tablas.tarea.metodos_tarea import crear_tarea, obtener_tareas, modificar_tarea, obtener_tareas, eliminar_tarea

def menu_tareas(usuario):
    while True:
        limpiar_consola()
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
            print("Opción inválida. Intente nuevamente.")

menu_tareas()

def obtener_datos_tarea(usuario):
    """
    Obtiene los datos necesarios para crear una tarea, incluyendo título, descripción, 
    fecha de finalización, usuario asignado y proyecto asociado. La función solicita la 
    entrada del usuario para cada campo, validando la entrada para asegurarse de que sea 
    válida. Luego, selecciona el proyecto asociado a partir de una lista de proyectos 
    disponibles para el usuario y devuelve un arreglo con todos los datos recopilados. 

    """

    titulo_tarea = input("Ingrese titulo de la tarea: ")

    while (not validar_texto(titulo_tarea, "titulo")):
        titulo_tarea = input("Ingresar titulo de la tarea: ")
        
    descripcion_tarea = input("Ingrese descripcion de la tarea: ")

    while (not validar_texto(descripcion_tarea, "descripción")):
        descripcion_tarea = input("Ingresar descripción de la tarea: ")

    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while not validar_fecha(end_date):
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    uuid_usuario = usuario['uuid']
    equipo_del_usuario = obtener_equipo_por_usuario(uuid_usuario)
    uuid_equipo = equipo_del_usuario["uuid"]
    proyectos_del_equipo = obtener_proyectos(uuid_equipo)

    proyecto_seleccionado = None
    
    while not proyecto_seleccionado:
        print("Seleccione el proyecto al que desea asignar la tarea: ")

        for proyecto in proyectos_del_equipo:
            print(f"Proyecto: {proyecto['nombre']}")

        nombre_proyecto = input("Ingrese el nombre del proyecto: ")

        for proyecto in proyectos_del_equipo:
            if proyecto['nombre'] == nombre_proyecto:
                proyecto_seleccionado = proyecto
                break
        
        if proyecto_seleccionado == None:
            print("Proyecto no encontrado.")

    return [
        titulo_tarea,
        descripcion_tarea,
        uuid_usuario,
        proyecto_seleccionado['uuid'],
        end_date,
    ]

