def obtener_proyectos(id_equipo):
    return 'proyectos'

def obtener_proyecto(id_proyecto):
    return 'proyecto'

def crear_proyecto():
    """
    Funciones para crear proyecto
    """
    id_proyecto = int(input("Ingrese id proyecto: "))
    nombre_proyecto = input("Ingresar nombre del proyecto: ")
    created_at = int(input("Ingrese fecha de creacion de proyecto: "))
    end_date = int(input("Ingrese fecha finalizacion proyecto: "))
    
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