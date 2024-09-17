from ..equipo.metodos_equipo import obtener_equipo_por_usuario
from misc.metodos_uuid import generar_uuid
from misc.metodos_validacion import validar_fecha
from ..proyecto.metodos_proyecto import obtener_proyectos
from datetime import datetime

matriz_tareas = []

def obtener_tareas():
    return 'tareas'

def obtener_tarea(id_tarea):
    return 'tarea'

def obtener_tareas_usuario(id_usuario):
    return 'tareas'

def crear_tarea():
    """
        Funcion para crear una tarea

        Retorna:
            string: uuid de la tarea creada
    """

    """ TODO: Definir de donde se saca el id del usuario """
    id_tarea = generar_uuid()
    titulo_tarea = input("Ingrese titulo de la tarea: ")
    descripcion_tarea = input("Ingrese descripcion de la tarea: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    id_usuario = 1
    equipo_del_usuario = obtener_equipo_por_usuario(id_usuario)
    id_equipo = equipo_del_usuario["uuid"]
    proyectos_del_equipo = obtener_proyectos(id_equipo)

    proyecto_seleccionado = None
    
    while proyecto_seleccionado == None:
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

    #Almacenar en matrices 
    tarea = [
        id_tarea,
        titulo_tarea,
        descripcion_tarea,
        id_usuario,
        proyecto_seleccionado,
        created_at,
        end_date,
    ]
    matriz_tareas.append(tarea)
    print(f"Creando tarea para el proyecto: {proyecto_seleccionado}")
    show_matrix = lambda matrix: print("\n".join([" | ".join([str(element) for element in row]) for row in matrix]))
    show_matrix(matriz_tareas)

def modificar_tarea(tarea):  
    """
    Función para modificar los datos de una tarea existente.
    Se puede modificar el titulo, descripcion, el proyecto asignado, usuario asignado y fecha de finalizacion.
    """
    print(f"Datos actuales del usuario: {tarea}")
    opcion = input("¿Qué desea modificar? (titulo/descripcion/id_proyecto/id_usuario/end_date): ").lower()

    if opcion == "titulo":
        tarea["titulo"] = input("Ingresar nuevo titulo de la tarea: ")
    elif opcion == "descripcion":
        tarea["descripcion"] = input("Ingresar nueva descripcion de la tarea: ")
    elif opcion == "id_proyecto":
        tarea["id_proyecto"] = input("Ingresar nuevo id del proyecto de la tarea: ")
    elif opcion == "id_usuario":
        tarea["id_usuario"] = input("Ingresar nuevo id del usario asignado a la tarea: ")    
    elif opcion == "end_date":
        tarea["end_date"] = input("Ingresar nueva end date de la tarea: ")
    else:
        print("Opción no válida.")

    return tarea

def asignar_usuario_tarea(id_tarea, id_usuario):
    return 'success'

def asignar_proyecto_tarea(id_proyecto):
    return 'success'

def eliminar_tarea(id_tarea):
    return 'success'