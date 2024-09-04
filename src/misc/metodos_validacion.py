from datetime import datetime

def validar_fecha(fecha):
    """
        Funcion para validar fecha

        Retorna:
            booleano
    """

    try:
        datetime.strptime(fecha, '%d-%m-%Y')
        return True
    except:
        print("Error: Formato de fecha incorrecto")
        return False
    