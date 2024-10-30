import json
from datetime import datetime
from src.misc.metodos_uuid import generar_uuid
from src.misc.metodos_os import obtener_ruta
"""from src.modulos.proyectos.modulo_proyecto import obtener_datos_proyecto"""

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
        Función para crear un proyecto y guardarlo en un archivo JSON.
        
    """

    id_proyecto = generar_uuid()
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    #Diccionario proyecto
    # Revisar si agregar equipo o no / pedir asignar equipo al proyecto
    proyecto = {
        "id": id_proyecto,
        "nombre": nombre_proyecto,
        "created_at": created_at,
        "end_date": end_date,
        "deleted_at": None
    }
    
    try:

        #  Abre el archivo y carga los proyectos desde el archivo JSON
        with open(RUTA_ABSOLUTA_PROYECTOS, 'r', encoding='UTF-8') as archivo_json:
            proyectos = json.load(archivo_json)
            if not isinstance(proyectos, list):
                print("Error: El archivo JSON no contiene una lista de proyectos.")
                proyectos = []

        proyectos.append(proyecto)

        # Agregar el nuevo proyecto a la lista de proyectos
        with open(RUTA_ABSOLUTA_PROYECTOS, 'w', encoding='UTF-8') as archivo_json:
            json.dump(proyectos, archivo_json, ensure_ascii=False, indent =4) # "ensure_ascii" para evitar la codificación de los caracteres en formato Unicode

    except json.JSONDecodeError as e:
        print("El archivo JSON está mal formateado:", e)    
    except (FileNotFoundError, OSError) as e:
        print("Ocurrió un error:", e)
    
    else:
        print("El proyecto se ha creado y guardado correctamente")

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
