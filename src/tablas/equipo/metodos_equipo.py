import json
from misc.metodos_os import obtener_ruta 

RUTA_ABSOLUTA_EQUIPOS = obtener_ruta('equipos.json')

def obtener_equipos():
    try:
        equipos_json = open(RUTA_ABSOLUTA_EQUIPOS, 'r', encoding='UTF-8')

        equipos = json.load(equipos_json)

        equipos_json.close()

        return equipos
    except Exception as e:
        raise Exception('Error al obtener los equipos: \n', e)
    
def obtener_equipo(uuid_equipo):
    try:
        equipos = obtener_equipos()

        for equipo in equipos:
            if equipo['uuid'] == uuid_equipo:
                return equipo
            
        return None
    except Exception as e:
        raise Exception('Error al obtener el equipo: \n', e)

def crear_equipo(equipo):
    try:
        equipos_json = open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8')

        equipos = json.load(equipos_json)

        equipos.append(equipo)
        
        equipos_json.seek(0)

        json.dump(equipos, equipos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al crear el equipo: \n', e)
    
def modificar_equipo(uuid_equipo, equipo):
    try:
        equipos_json = open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8')

        equipos = json.load(equipos_json)

        equipo = next((equipo for equipo in equipos if equipo['uuid'] == uuid_equipo), None)

        if (not equipo):
            raise Exception('No se encontró el equipo')

        equipos_json.seek(0)

        json.dump(equipos, equipos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al modificar el equipo: \n', e)
    
def eliminar_equipo(uuid_equipo):
    try:
        equipos_json = open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8')

        equipos = json.load(equipos_json)

        equipo = next((equipo for equipo in equipos if equipo['uuid'] == uuid_equipo), None)

        if (not equipo):
            raise Exception('No se encontró el equipo')

        equipos.remove(equipo)

        equipos_json.seek(0)

        json.dump(equipos, equipos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al eliminar el equipo: \n', e)