from misc.metodos_visualizacion import visualizar_matriz
from misc.metodos_os import  obtener_ruta
import json
  
RUTA_ABSOLUTA_TAREAS = obtener_ruta('tareas.json')

def obtener_tareas():
    try:
        tareas_json = open(RUTA_ABSOLUTA_TAREAS, 'r', encoding='UTF-8')

        tareas = json.load(tareas_json)

        tareas_json.close()

        return  tareas
    except Exception as e:
        raise Exception('Error al obtener las tareas: \n', e)

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

        for tarea in tareas:
            if tarea['uuid_usuario'] == uuid_usuario:
                return tarea
            
        return None
    except Exception as e:
        raise Exception('Error al obtener la tarea: \n', e)

def crear_tarea(tarea):
    try:
        tareas_json = open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8')

        tareas = json.load(tareas_json)

        tareas.append(tarea)
        
        tareas_json.seek(0)

        json.dump(tareas, tareas_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al crear la tarea: \n', e)

def modificar_tarea(nueva_tarea):  
    try:
        tareas_json = open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8')

        tareas = json.load(tareas_json)

        tarea = next((equipo for equipo in tareas if equipo['uuid'] == nueva_tarea["uuid"]), None)

        if (not tarea):
            raise Exception('No se encontró el equipo')
        
        tareas[tareas.index(tarea)] = nueva_tarea

        tareas_json.seek(0)

        json.dump(tareas, tareas_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al modificar la tarea: \n', e)

def asignar_usuario_tarea(uuid_tarea, id_usuario):
    return 'success'

def asignar_proyecto_tarea(id_proyecto):
    return 'success'

def eliminar_tarea(uuid_tarea):
    try:
        tareas_json = open(RUTA_ABSOLUTA_TAREAS, 'r+', encoding='UTF-8')

        tareas = json.load(tareas_json)

        tarea = next((tarea for equipo in tareas if equipo['uuid'] == uuid_tarea), None)

        if (not tarea):
            raise Exception('No se encontró la tarea')

        tareas.remove(tarea)

        tareas_json.seek(0)

        json.dump(tareas, tareas_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al eliminar la tarea: \n', e)
