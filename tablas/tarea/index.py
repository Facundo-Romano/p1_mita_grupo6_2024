def obtener_tareas():
    return 'tareas'

def obtener_tarea(id_tarea):
    return 'tarea'

def obtener_tareas_usuario(id_usuario):
    return 'tareas'

def crear_tarea(tarea):
    """
    Creacion de tarea usando diccionario, contiene el id, nombre, la fecha de creacion, 
    la fecha de fin. 
    """
    #Esta es una funcion para validar que haya un proyecto al cual asignar la tarea.
    #Porque no puede existir una tarea sin que exista un proyecto a la cual asignarle.
    id_proyecto = int(input("Ingrese id del proyecto al cual le va a asignar la tarea: "))
    while id_proyecto not in proyectos: #Tenemos que importar la lista de proyectos
        id_proyecto = int(input("Ese proyecto no existe, Ingrese id del proyecto al cual le va a asignar la tarea: "))
    else:
        id_tarea = int(input("Ingrese id proyecto: "))
        titulo_tarea = input("Ingresar nombre del proyecto: ")
        descripcion_tarea = input("Ingresar nombre del proyecto: ")
        id_usuario = int(input("Ingrese ID del usuario asignado a la tarea: "))
        created_at = int(input("Ingrese fecha de creacion de proyecto: "))
        end_date = int(input("Ingrese fecha finalizacion proyecto: "))

    #Diccionario tarea
    tarea = {
        "id": id_tarea,
        "titulo": titulo_tarea,
        "descripcion": descripcion_tarea,
        "id_proyecto": id_proyecto,
        "id_usuario": id_usuario,
        "created_at": created_at,
        "end_date": end_date
    }
    return tarea

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