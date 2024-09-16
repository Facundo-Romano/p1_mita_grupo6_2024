from datetime import datetime
import re

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
    

def validar_mail(mail):
    """
        Funcion para validar mail

        Retorna:
            booleano
    """

    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(email_regex, mail):
        print("Error: Formato de mail incorrecto")
        return False

    return True

def validar_contraseña(contraseña):
    """
        Funcion para validar contraseña

        Retorna:
            booleano
    """

    contraseña_regex = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if not re.match(contraseña_regex, contraseña):
        print("Error: Formato de contraseña incorrecto")
        return False

    return True

def validar_texto(texto, tipo):
    """
        Funcion para validar texto,
        si el texto es alfabético retorna True, si no, retorna False
        si texto no es formato string retorna False

        Retorna:
            booleano
    """

    try:
        if texto.isalpha():
            return True
    
        print(f"Error: Formato de {tipo} incorrecto")
        return False
    except:
        print(f"Error: Formato de {tipo} incorrecto")
        return False