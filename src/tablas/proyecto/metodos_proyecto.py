from datetime import datetime
from misc.metodos_uuid import generar_uuid
from misc.metodos_validacion import validar_fecha
from modulos.proyectos.modulo_proyecto import obtener_datos_proyecto

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
    return 'proyecto'

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

    return proyecto

def modificar_proyecto(proyecto):
    return 'success'

def eliminar_proyecto(id_proyecto):
    return 'success'