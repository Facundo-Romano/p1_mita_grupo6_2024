from datetime import datetime
from misc.metodos_uuid import generar_uuid
from modulos.proyectos.modulo_proyecto import obtener_datos_proyecto

#Contiene la Lista de Diccionarios (lista de todos los proyectos)
proyectos = []

def obtener_proyectos(id_equipo):
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

    return proyectos

def obtener_proyecto(id_proyecto):
    for proyecto in proyectos:
        if proyecto['uuid'] == id_proyecto and proyecto['deleted_at'] is None:
            return proyecto
    return None

def crear_proyecto():
    """
        Funcion para crear un proyecto

        Retorna:
            string: uuid del proyecto creado
    """

    id_proyecto = generar_uuid()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    [nombre_proyecto, end_date] = obtener_datos_proyecto()
    """Para reutilizar código"""

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
    
    [nombre_proyecto, end_date] = obtener_datos_proyecto()

#Ver de si faltan o no campos (o atributos)
    nuevo_proyecto = [
        proyecto[0], #uuid
        nombre_proyecto,
        proyecto[2],
        end_date
    ]

    index = proyectos.index(proyecto)
    proyectos[index] = nuevo_proyecto
    

def eliminar_proyecto(id_proyecto):
    return 'success'

#Prueba de Código
modificar_proyecto('test2') #Borrar más tarde
