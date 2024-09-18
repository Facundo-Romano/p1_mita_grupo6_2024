from misc.metodos_uuid import generar_uuid
from modulos.tareas.modulo_tareas import obtener_datos_tarea
from misc.metodos_visualizacion import visualizar_matriz
from datetime import datetime

MATRIZ_TAREAS = [
    ['uuid_prueba', 'titulo', 'descripcion', 'uuid_usuario', 'uuid_proyecto', 'created_at', 'end_date'],
    ['9p8uwheqc97g48d1v', 'primer tarea', 'la mejor tarea', 'erv234v2t2t', '4t5gb254bv4twv4tw ', '2024-09-17 18:35:11', '12-12-2024'],
]

def obtener_tareas():
    """
    Convierte una matriz de tareas en una lista de diccionarios, donde 
    cada diccionario representa una tarea. La función toma la matriz de 
    tareas, separa los headers de las filas, y luego itera sobre cada 
    fila para crear un diccionario que asigna cada valor de la fila a su 
    respectivo header. Finalmente, devuelve una lista de estos diccionarios, 
    permitiendo un acceso más fácil y legible a los datos de las tareas. 
    """
    headers = MATRIZ_TAREAS[0]  # Headers de la matriz
    tareas = MATRIZ_TAREAS[1:]  # Filas de la matriz, excluyendo headers
    
    tareas_dict = []
    '''
    la variable zip toma las listas headers y tarea y las empareja en tuplas.
    Luego dict covierte las tuplas generadas por zip en pares clave-valor para crear un diccionario.

    '''
    for tarea in tareas:
        tarea_dict = dict(zip(headers, tarea))  # Crea un diccionario para cada tarea
        tareas_dict.append(tarea_dict)
    
    return tareas_dict

def obtener_tarea(uuid_tarea):
    """
    Busca una tarea por el UUID, itera  sobre la lista de tareas 
    y verifica si el primer elemento de la fila (UUID) coincide 
    con el UUID de la tarea buscada. Si se encuentra una coincidencia,
    devuelve la tarea completa. Si no se encuentra ninguna tarea que 
    coincida, devuelve None.

    """
    for tarea in MATRIZ_TAREAS:
        if tarea[0] == uuid_tarea:
            return tarea

    return None

def obtener_tareas_usuario(id_usuario):
    return 'tareas'

def crear_tarea():
    """
    Crea una nueva tarea y la agrega a la matriz de tareas. La función genera un 
    UUID único para la tarea y se genera la fecha de creacion, y luego solicita 
    los datos de la tarea mediante la función obtener_datos_tarea(). Luego, crea 
    una nueva fila en la matriz de tareas con los datos proporcionados y la agrega 
    a la matriz. Finalmente, llama a la función visualizar_matriz() para mostrar la 
    matriz de tareas actualizada.
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
        Se puede modificar el titulo, descripcion, el proyecto 
        asignado, usuario asignado y fecha de finalizacion.
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
    """
    Elimina una tarea de la matriz de tareas,  si la tarea no existe
    se muestra un mensaje de error.
    """
    tarea = obtener_tarea(uuid_tarea)

    if not tarea:
        return print("Error: tarea no encontrada.")

    index = MATRIZ_TAREAS.index(tarea)

    MATRIZ_TAREAS.pop(index)
    print("Tarea eliminada exitosamente")
