import json
from src.misc.metodos_os import obtener_ruta 
from src.misc.metodos_formateo_datos import convertir_a_lista 

RUTA_ABSOLUTA_EQUIPOS = obtener_ruta('equipos.json')

def obtener_equipos():
    try:
        with open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8') as equipos_json:

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
        with open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8') as equipos_json:
            equipos = json.load(equipos_json)

            equipos.append(equipo)

            equipos = convertir_a_lista(equipos)
            
            equipos_json.seek(0)
            equipos_json.truncate()

            json.dump(equipos, equipos_json, indent=4)

            print("\nEquipo creado exitosamente\n")

        return True
    except Exception as e:
        raise Exception('Error al crear el equipo: \n', e)
    
def modificar_equipo(nuevo_equipo):
    try:
        with open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8') as equipos_json:

            equipos = json.load(equipos_json)

            equipo = next((equipo for equipo in equipos if equipo['uuid'] == nuevo_equipo["uuid"]), None)

            if (not equipo):
                raise Exception('No se encontró el equipo')
            
            equipos[equipos.index(equipo)] = nuevo_equipo

            equipos_json.seek(0)
            equipos_json.truncate()

            json.dump(equipos, equipos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al modificar el equipo: \n', e)
    
def eliminar_equipo(uuid_equipo):
    try:
        with open(RUTA_ABSOLUTA_EQUIPOS, 'r+', encoding='UTF-8') as equipos_json:

            equipos = json.load(equipos_json)

            equipo = next((equipo for equipo in equipos if equipo['uuid'] == uuid_equipo), None)

            if (not equipo):
                raise Exception('No se encontró el equipo')

            equipos.remove(equipo)
            
            equipos = convertir_a_lista(equipos)

            equipos_json.seek(0)
            equipos_json.truncate()

            json.dump(equipos, equipos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al eliminar el equipo: \n', e)