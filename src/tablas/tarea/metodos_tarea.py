from ..equipo.metodos_equipo import obtener_equipo_por_usuario
from ..proyecto.metodos_proyecto import obtener_proyectos

def obtener_tareas():
    return 'tareas'

def obtener_tarea(id_tarea):
    return 'tarea'

def obtener_tareas_usuario(id_usuario):
    return 'tareas'

def crear_tarea(tarea):
    """
        Funcion para crear una tarea

        Retorna:
            string: uuid de la tarea creada
    """

    """ TODO: Definir de donde se saca el id del usuario """
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
    
    print("Creando tarea para el proyecto: ", proyecto_seleccionado)

    




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