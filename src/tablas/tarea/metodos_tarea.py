from misc.metodos_uuid import generar_uuid
from modulos.tareas.modulo_tareas import obtener_datos_tarea
from misc.metodos_visualizacion import visualizar_matriz
from datetime import datetime

MATRIZ_TAREAS = [
    ['uuid_prueba', 'titulo', 'descripcion', 'uuid_usuario', 'uuid_proyecto', 'created_at', 'end_date'],
    ['9p8uwheqc97g48d1v', 'primer tarea', 'la mejor tarea', 'erv234v2t2t', '4t5gb254bv4twv4tw ', '2024-09-17 18:35:11', '12-12-2024'],
]

def obtener_tareas():
    return 'tareas'

def obtener_tarea(uuid_tarea):
    for tarea in MATRIZ_TAREAS:
        if tarea[0] == uuid_tarea:
            return tarea

    return None

def obtener_tareas_usuario(id_usuario):
    return 'tareas'

def crear_tarea():
    """
        Funcion para crear una tarea

        Retorna:
            string: uuid de la tarea creada
    """

    id_tarea = generar_uuid()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    [titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date] = obtener_datos_tarea()

    #Almacenar en matrices 
    tarea = [
        id_tarea,
        titulo_tarea,
        descripcion_tarea,
        uuid_usuario,
        uuid_proyecto,
        created_at,
        end_date,
    ]

    MATRIZ_TAREAS.append(tarea)

    visualizar_matriz(MATRIZ_TAREAS)

def modificar_tarea(uuid_tarea):  
    """
        Función para modificar los datos de una tarea existente.
        Se puede modificar el titulo, descripcion, el proyecto asignado, usuario asignado y fecha de finalizacion.
    """

    tarea = obtener_tarea(uuid_tarea)

    if not tarea:
        return print("Error: tarea no encontrada.")

    [titulo_tarea, descripcion_tarea, uuid_usuario, uuid_proyecto, end_date] = obtener_datos_tarea()

    nueva_tarea = [
        tarea[0],
        titulo_tarea,
        descripcion_tarea,
        uuid_usuario,
        uuid_proyecto,
        tarea[5],
        end_date,
    ]

    index = MATRIZ_TAREAS.index(tarea)

    MATRIZ_TAREAS[index] = nueva_tarea
    
def asignar_usuario_tarea(id_tarea, id_usuario):
    return 'success'

def asignar_proyecto_tarea(id_proyecto):
    return 'success'

def eliminar_tarea(uuid_tarea):
    tarea = obtener_tarea(uuid_tarea)

    if not tarea:
        return print("Error: tarea no encontrada.")

    index = MATRIZ_TAREAS.index(tarea)

    MATRIZ_TAREAS.pop(index)

    print(MATRIZ_TAREAS)
