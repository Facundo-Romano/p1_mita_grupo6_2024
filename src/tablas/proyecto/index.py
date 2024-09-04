from ..misc.metodos_uuid import generar_uuid

def obtener_proyectos(id_equipo):
    return 'proyectos'

def obtener_proyecto(id_proyecto):
    return 'proyecto'

def crear_proyecto():
    """
    Funciones para crear proyecto
    """
    nombre_proyecto = input("Ingresar nombre del proyecto: ")
    end_date = int(input("Ingrese fecha finalizacion proyecto: "))

    id_proyecto = generar_uuid()

    print(id_proyecto)
    
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


crear_proyecto()