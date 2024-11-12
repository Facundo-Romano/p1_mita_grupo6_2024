from datetime import datetime
import re

def validar_fecha(fecha):
    """
    Convierte una cadena de texto con formato 'dd-mm-YYYY' en un objeto datetime.

    Parámetros:
    - fecha (str): Cadena de texto que contiene la fecha, en formato 'día-mes-año' (por ejemplo, '18-09-2024').

    Retorna:
    - datetime: Un objeto datetime que representa la fecha proporcionada.

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
        print("Error: Formato de contraseña incorrecto\n" "Error: La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial (@, $, !, %, *, ?, &).")
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
        if texto.replace(" ", "").isalpha():
            return True
    
        print(f"Error: Formato de {tipo} incorrecto")
        return False
    except:
        print(f"Error: Formato de {tipo} incorrecto")
        return False