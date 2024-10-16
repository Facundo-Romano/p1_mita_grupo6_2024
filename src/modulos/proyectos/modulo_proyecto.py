from misc.metodos_validacion import validar_texto, validar_fecha

def obtener_datos_proyecto():
    """
    Obtiene los datos necesarios para crear un proyecto.
    Retorna una lista con los elementos introducidos.
    """

    nombre_proyecto = input("Ingresar nombre del proyecto: ")

    while (not validar_texto(nombre_proyecto, "nombre")):
        nombre_proyecto = input("Ingresar nombre del proyecto: ")
    
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")
    
    return [nombre_proyecto, end_date]