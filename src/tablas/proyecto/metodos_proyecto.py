import json
from datetime import datetime
from misc.metodos_uuid import generar_uuid
from misc.metodos_os import obtener_ruta
"""from modulos.proyectos.modulo_proyecto import obtener_datos_proyecto"""

RUTA_ABSOLUTA_PROYECTOS = obtener_ruta('proyectos.json')

#Contiene la Lista de Diccionarios (lista de todos los proyectos)
"""
proyectos = [
        {
            'uuid': 'test1',
            'nombre': 'proyecto1',
            'uuid_equipo': 'equipo1',
            'end_date': '09-08-2025',
            'created_at': '2021-08-09 12:00:00',
            'deleted_at': None
        },
        {
            'uuid': 'test2',
            'nombre': 'proyecto2',
            'uuid_equipo': 'equipo1',
            'end_date': '09-08-2025',
            'created_at': '2021-08-09 12:00:00',
            'deleted_at': None
        }
    ]
"""

def obtener_proyectos():
    try:
        with open(RUTA_ABSOLUTA_PROYECTOS, 'r', encoding='UTF-8') as archivo_json:
            proyectos = json.load(archivo_json)
            return proyectos

    except FileNotFoundError as e:
        print("No se ha encontrado el archivo:",e)
        return [] # Retorna una lista vacia en vez de None para que no ocurra error en otra funcion (obtener_proyecto).
    except OSError as e:
        print("Ha ocurrido un error:",e)
        return []

def obtener_proyecto(id_proyecto):
    try:
        proyectos = obtener_proyectos()
    
    except:
        print("Error inesperado")

    else:
        for proyecto in proyectos:
            if proyecto['uuid'] == id_proyecto and proyecto['deleted_at'] is None:
                return proyecto
        return None

def crear_proyecto(nombre_proyecto, end_date):
    """
        Funcion para crear un proyecto
        Retorna:
            Diccionario con la información del proyecto creado.
    """

    id_proyecto = generar_uuid()
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #Diccionario proyecto
    proyecto = {
        "id": id_proyecto,
        "nombre": nombre_proyecto,
        "created_at": created_at,
        "end_date": end_date
    }
    proyectos.append(proyecto)
    return proyecto

def modificar_proyecto(id_proyecto):
    """
        Función para modificar los datos de un proyecto existente.
        Se puede modificar el titulo, descripcion, el proyecto 
        asignado, usuario asignado y fecha de finalizacion.
    """
    proyecto = obtener_proyecto(id_proyecto)

    if not proyecto:
        return print("Error: proyecto no encontrado.")
    
    # Eliminar obtener datos
    """[nombre_proyecto, end_date] = obtener_datos_proyecto()"""

    nuevo_proyecto = [
        proyecto['uuid'], #uuid
        nombre_proyecto,
        proyecto['uuid_equipo'],
        end_date
    ]

    index = proyectos.index(proyecto)
    proyectos[index] = nuevo_proyecto
    

def eliminar_proyecto(id_proyecto):
    return 'success'
