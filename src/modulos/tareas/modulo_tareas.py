from misc.metodos_validacion import validar_fecha, validar_texto
from tablas.equipo.metodos_equipo import obtener_equipo_por_usuario
from tablas.proyecto.metodos_proyecto import obtener_proyectos

def obtener_datos_tarea():
    """
    Obtiene los datos necesarios para crear una tarea, incluyendo título, descripción, 
    fecha de finalización, usuario asignado y proyecto asociado. La función solicita la 
    entrada del usuario para cada campo, validando la entrada para asegurarse de que sea 
    válida. Luego, selecciona el proyecto asociado a partir de una lista de proyectos 
    disponibles para el usuario y devuelve un arreglo con todos los datos recopilados. 

    """

    titulo_tarea = input("Ingrese titulo de la tarea: ")

    while (not validar_texto(titulo_tarea, "titulo")):
        titulo_tarea = input("Ingresar titulo de la tarea: ")
        
    descripcion_tarea = input("Ingrese descripcion de la tarea: ")

    while (not validar_texto(descripcion_tarea, "descripción")):
        descripcion_tarea = input("Ingresar descripción de la tarea: ")

    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while not validar_fecha(end_date):
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    uuid_usuario = 1
    equipo_del_usuario = obtener_equipo_por_usuario(uuid_usuario)
    uuid_equipo = equipo_del_usuario["uuid"]
    proyectos_del_equipo = obtener_proyectos(uuid_equipo)

    proyecto_seleccionado = None
    
    while not proyecto_seleccionado:
        print("Seleccione el proyecto al que desea asignar la tarea: ")

        for proyecto in proyectos_del_equipo:
            print(f"Proyecto: {proyecto['nombre']}")

        nombre_proyecto = input("Ingrese el nombre del proyecto: ")

        for proyecto in proyectos_del_equipo:
            if proyecto['nombre'] == nombre_proyecto:
                proyecto_seleccionado = proyecto
                break
        
        if proyecto_seleccionado == None:
            print("Proyecto no encontrado.")

    return [
        titulo_tarea,
        descripcion_tarea,
        uuid_usuario,
        proyecto_seleccionado['uuid'],
        end_date,
    ]