from datetime import datetime
from src.misc.metodos_validacion import validar_fecha, validar_texto
from src.misc.metodos_uuid import generar_uuid
from src.misc.metodos_visualizacion import mostrar_tareas, limpiar_consola, mostrar_detalle_tarea
from src.misc.metodos_obtencion_datos import obtener_numero
from src.tablas.tarea.metodos_tarea import crear_tarea, modificar_tarea, eliminar_tarea, obtener_tareas_usuario
from src.tablas.proyecto.metodos_proyecto import obtener_proyecto
from src.tablas.proyecto.metodos_proyecto import obtener_proyectos_por_usuario

def menu_tareas(usuario):
    limpiar_consola()
    while True:
        print(f"\n\n\nMenú de tareas")
        print("1. Mis tareas")
        print("2. Detalle de una tarea")
        print("3. Crear nueva tarea")
        print("4. Editar tarea")
        print("5. Eliminar tarea")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_mis_tareas(usuario["uuid"])
        elif opcion == "2":
            detalle_de_tarea(usuario)
        elif opcion == "3":
            crear_nueva_tarea(usuario)
        elif opcion == "4":
            editar_tarea(usuario)
        elif opcion == "5":
            eliminacion_tarea(usuario["uuid"])
        elif opcion == "6":
            limpiar_consola()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_tarea(usuario):
    """
    Obtiene los datos necesarios para crear una tarea, incluyendo título, descripción, 
    fecha de finalización, usuario asignado y proyecto asociado. La función solicita la 
    entrada del usuario para cada campo, validando la entrada para asegurarse de que sea 
    válida. Luego, selecciona el proyecto asociado a partir de una lista de proyectos 
    disponibles para el usuario y devuelve un arreglo con todos los datos recopiladoss. 

    """
    limpiar_consola()

    titulo_tarea = input("Ingrese título de la tarea: ")

    while (not validar_texto(titulo_tarea, "titulo")):
        titulo_tarea = input("Ingresar titulo de la tarea: ")
        
    descripcion_tarea = input("Ingrese descripcion de la tarea: ")

    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while not validar_fecha(end_date):
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    subtarea = obtener_subtarea()

    uuid_usuario = usuario['uuid']
    proyectos_del_equipo = obtener_proyectos_por_usuario(usuario["uuid_equipo"])

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

    return (
        titulo_tarea,
        descripcion_tarea,
        uuid_usuario,
        proyecto_seleccionado['uuid'],
        end_date,
        subtarea,
    )

def obtener_subtarea():
    subtarea = None

    print('Queres crear una nueva subtarea?')
    si_o_no =  input('s/n?: ')

    if si_o_no.lower() == 's':
        nombre = input('Ingrese nombre de la subtarea: ')
        while (not validar_texto(nombre, 'nombre')):
            nombre = input('Ingrese nombre de la subtarea: ')
        descripcion = input('Ingrese descripcion de la subtarea: ')
        subtarea_subtarea = obtener_subtarea()

        subtarea = {
            'nombre': nombre,
            'descripcion':  descripcion,
            'subtarea':  subtarea_subtarea
        }
    elif  si_o_no.lower() != 'n':
        print('Opcion invalida')
        return obtener_subtarea()
    
    return subtarea

def mostrar_mis_tareas(uuid_usuario):
    tareas = obtener_tareas_usuario(uuid_usuario)
    limpiar_consola()
    print("Mis tareas: ")
    mostrar_tareas(tareas)

def detalle_de_tarea(usuario):
    tareas = obtener_tareas_usuario(usuario["uuid"])
    limpiar_consola()
    print("Mis tareas: ")
    mostrar_tareas(tareas)

    numero = obtener_numero("\n\nIngrese el número de la tarea a ver en detalle: ", 1, len(tareas))
    
    tarea = tareas[numero - 1]

    proyecto = obtener_proyecto(tarea["uuid_proyecto"])
    

    limpiar_consola()
    mostrar_detalle_tarea(tarea, proyecto)

def crear_nueva_tarea(usuario):
    (titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date, subtarea) = obtener_datos_tarea(usuario)
    
    tarea = {
        "uuid" :  generar_uuid(),
        "titulo": titulo_tarea,
        "descripcion": descripcion_tarea,
        "uuid_usuario": uuid_usuario,
        "uuid_proyecto": uuid_proyecto,
        "created_at":  datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "end_date": end_date,
        "subtarea": subtarea
    }

    limpiar_consola()
    print("Creando tarea...")
    crear_tarea(tarea)
    print("Tarea creada exitosamente!")

def editar_tarea(usuario):
    tareas = obtener_tareas_usuario(usuario["uuid"])

    limpiar_consola()
    print("Tareas disponibles para modificar: ")
    mostrar_tareas(tareas)

    numero = obtener_numero("\n\nIngrese el número de la tarea a modificar: ", 1, len(tareas))
    
    tarea_a_modificar = tareas[numero - 1]

    limpiar_consola()
    print("Tarea a modificar: ")
    mostrar_tareas([tarea_a_modificar])

    (titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date, subtarea) = obtener_datos_tarea(usuario)

    tarea = {
        "uuid": tarea_a_modificar["uuid"],
        "titulo": titulo_tarea,
        "descripcion": descripcion_tarea,
        "uuid_usuario": uuid_usuario,
        "uuid_proyecto": uuid_proyecto,
        "created_at": tarea_a_modificar["created_at"],
        "end_date": end_date,
        "subtarea": subtarea
    }

    print("\n\nModificanbdo tarea...")
    modificar_tarea(tarea)    
    print("Tarea modificada exitosamente!")

def eliminacion_tarea(uuid_usuario):
    tareas = obtener_tareas_usuario(uuid_usuario)

    limpiar_consola()
    print("Tareas disponibles para eliminar: ")
    mostrar_tareas(tareas)

    numero = obtener_numero("\nIngrese el número de la tarea a eliminar: ", 1, len(tareas))
    
    tarea_a_eliminar = tareas[numero - 1]

    limpiar_consola()
    print("Tarea a eliminar: ")
    mostrar_tareas([tarea_a_eliminar])
    confirmacion = input('\n¿Está seguro que desea eliminar la tarea? (s/n)')

    if confirmacion == 's':
        limpiar_consola()
        print("Eliminando tarea...")
        eliminar_tarea(tarea_a_eliminar['uuid'])
        print("Tarea eliminada exitosamente!")
    elif confirmacion == 'n':
        print('Eliminación cancelada')
    else:
        print('Opción inválida')
        eliminar_tarea(uuid_usuario)
