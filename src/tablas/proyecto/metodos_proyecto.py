from datetime import datetime
from ...misc.metodos_uuid import generar_uuid
from ...misc.metodos_validacion import validar_fecha

def obtener_proyectos(id_equipo):
    return 'proyectos'

def obtener_proyecto(id_proyecto):
    return 'proyecto'

def crear_proyecto():
    """
        Funcion para crear un proyecto

        Retorna:
            string: uuid del proyecto creado
    """

    id_proyecto = generar_uuid()
    nombre_proyecto = input("Ingresar nombre del proyecto: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    
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