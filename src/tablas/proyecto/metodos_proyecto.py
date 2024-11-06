import json
from src.misc.metodos_os import obtener_ruta
from src.misc.metodos_formateo_datos import convertir_a_lista 

RUTA_ABSOLUTA_PROYECTOS = obtener_ruta('proyectos.json')

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

def obtener_proyectos_por_equipo(uuid_equipo):
    try:
        proyectos = obtener_proyectos()
        proyectos_usuario = []  # Lista para almacenar las proyectos del usuario

        for proyecto in proyectos:
            if proyecto['uuid_equipo'] == uuid_equipo:
                proyectos_usuario.append(proyecto)  # Agregar la proyecto a la lista

        return proyectos_usuario  # Devolver la lista de proyectos del usuario
    except Exception as e:
        raise Exception('Error al obtener las proyectos del usuario: \n', e)

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

def crear_proyecto(proyecto):
    """
        Función para crear un proyecto y guardarlo en un archivo JSON.
        
    """
    try:
        proyectos_json = open(RUTA_ABSOLUTA_PROYECTOS, 'r+', encoding='UTF-8')

        proyectos = json.load(proyectos_json)

        proyectos.append(proyecto)

        proyectos = convertir_a_lista(proyectos)
        
        proyectos_json.seek(0)

        json.dump(proyectos, proyectos_json, indent=4)

        return True
    except Exception as e:
        raise Exception('Error al crear el equipo: \n', e)

def modificar_proyecto(proyecto):
    """
        Función para sobreescribir un proyecto especifico en la base de datos(JSON)
    """
    try:
        #Abro el archivo en modo lectura y escritura
        with open(RUTA_ABSOLUTA_PROYECTOS, 'r+', encoding='UTF-8') as archivo_json:
            proyectos = json.load(archivo_json)
        
            #Comparo los uuid
            proyecto = next((proyecto for proyecto in proyectos if proyecto["uuid"] == proyecto["uuid"]), None)

            if not proyecto:
                raise Exception("No se encontró el proyecto")

            proyectos[proyectos.index(proyecto)] = proyecto

            #Seek mueve el cursor ([cant bytes a moverse],[0=start; 1=cursor; 2=final])
            archivo_json.seek(0)
            
            # Escribo de nuevo la lista de proyectos en el archivo
            json.dump(proyectos, archivo_json, ensure_ascii=False, indent=4)
            
            print("El proyecto se modificó correctamente")

            # Truncar el archivo para eliminar contenido restante
            archivo_json.truncate()

    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")
    except Exception as e:
        print(f'Error al modificar el proyecto: {e}')
    
def eliminar_proyecto(proyecto_elim):
    try:
        #Abro el archivo en modo lectura y escritura
        with open(RUTA_ABSOLUTA_PROYECTOS, 'r+', encoding='UTF-8') as archivo_json:
            proyectos = json.load(archivo_json)
        
            #Comparo los uuid
            proyecto = next((proyecto for proyecto in proyectos if proyecto["uuid"]==proyecto_elim["uuid"]), None)

            if not proyecto:
                raise Exception("No se encontró el proyecto")
            
            #Elimino el proyecto
            proyectos.remove(proyecto)

            # Voy al inicio del archivo
            archivo_json.seek(0)

            json.dump(proyectos, archivo_json, ensure_ascii=False, indent=4)
            print("El proyecto se eliminó exitosamente")

            archivo_json.truncate()
        
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado.")
    except Exception as e:
        print(f'Error al modificar el proyecto: {e}')