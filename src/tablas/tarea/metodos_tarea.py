from src.misc.metodos_visualizacion import visualizar_matriz
from src.misc.metodos_os import  obtener_ruta
import json
  
RUTA_ABSOLUTA_TAREAS = obtener_ruta('tareas.json')

def crear_subtarea(subtarea, usuario):
    try:
        tarea = obtener_tareas_usuario(usuario)

        # Agregar la subtarea a la lista de subtareas
        tarea.setdefault('subtareas', []).append(subtarea)

        # Guardar las tareas actualizadas
        with open(RUTA_ABSOLUTA_TAREAS, 'w', encoding='UTF-8') as tareas_json:
            json.dump(tarea, tareas_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al crear la subtarea: \n', e)

def obtener_tareas():
    try:
        with open(RUTA_ABSOLUTA_TAREAS, 'r', encoding='UTF-8') as tareas_json:
            tareas = json.load(tareas_json)
            return tareas
    except Exception as e:
        raise Exception('Error al obtener las tareas: \n', e)
    finally:
        tareas_json.close()

def obtener_tarea(uuid_tarea):
    try:
        tareas = obtener_tareas()

        for tarea in tareas:
            if tarea['uuid'] == uuid_tarea:
                return tarea
            
        return None
    except Exception as e:
        raise Exception('Error al obtener la tarea: \n', e)

def obtener_tareas_usuario(uuid_usuario):
    try:
        tareas = obtener_tareas()
        tareas_usuario = []  # Lista para almacenar las tareas del usuario

        for tarea in tareas:
            if tarea['uuid_usuario'] == uuid_usuario:
                tareas_usuario.append(tarea)  # Agregar la tarea a la lista

        return tareas_usuario  # Devolver la lista de tareas del usuario
    except Exception as e:
        raise Exception('Error al obtener las tareas del usuario: \n', e)

def crear_tarea(tarea):
    try:
        # Abrir el archivo en modo lectura y escritura
        with open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8') as tareas_json:
            # Leer el contenido del archivo y verificar que no esté vacío
            contenido = tareas_json.read().strip()  # Leer y eliminar espacios en blanco

            if contenido == "":
                print("El archivo está vacío.")
            else:
                # Intentar cargar las tareas existentes
                tareas_json.seek(0)  # Asegúrate de estar al principio para leer
                tareas = json.load(tareas_json)

            tareas.append(tarea)  # Agregar la nueva tarea

            # Volver al principio del archivo para escribir
            tareas_json.seek(0)  
            json.dump(tareas, tareas_json, indent=4)  # Guardar las tareas

            tareas_json.truncate()  # Asegúrate de truncar el archivo después de escribir
            
        return True
    except json.JSONDecodeError:
        print("El archivo JSON está corrupto. Inicializando con una lista vacía.")
        with open(RUTA_ABSOLUTA_TAREAS, 'w', encoding='UTF-8') as tareas_json:
            tareas_json.write("[]")  # Inicializar con una lista vacía
    except Exception as e:
        print(f"Error: {e}")  # Imprimir el error para mayor claridad
        raise Exception('Error al crear la tarea: \n', e)

def modificar_tarea(nueva_tarea):  
    try:
        tareas_json = open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8')

        tareas = json.load(tareas_json)

        tarea_a_modificar = next((tarea for tarea in tareas if tarea['uuid'] == nueva_tarea["uuid"]), None)

        if (not tarea_a_modificar):
            raise Exception('No se encontró el equipo')
        
        tareas[tareas.index(tarea_a_modificar)] = nueva_tarea

        tareas_json.seek(0)
        tareas_json.truncate()

        json.dump(tareas, tareas_json, indent=4)
        
        return True
    except Exception as e:
        raise Exception('Error al modificar la tarea: \n', e)

def eliminar_tarea(uuid_tarea):
    try:
        with open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8') as tareas_json:
            tareas = json.load(tareas_json)

            # Busca la tarea con el UUID proporcionado
            tarea = next((tarea for tarea in tareas if tarea['uuid'] == uuid_tarea), None)

            if tarea is None:
                raise Exception('No se encontró la tarea')

            # Elimina la tarea de la lista
            tareas.remove(tarea)

            # Volver al principio del archivo para escribir
            tareas_json.seek(0)

            # Guardar las tareas actualizadas en el archivo
            json.dump(tareas, tareas_json, indent=4)

            # Truncar el archivo para eliminar el contenido restante
            tareas_json.truncate()
            
        return True
    except Exception as e:
        raise Exception('Error al eliminar la tarea: \n', e)