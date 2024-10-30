import os

def obtener_ruta(archivo, ambiente='produccion'):
    directorio_actual = os.getcwd()
    if (ambiente == 'produccion'):
        ruta_absoluta = os.path.join(directorio_actual, 'assets', archivo)
    else:
        ruta_absoluta = os.path.join(directorio_actual, 'assets', 'tests', archivo)

    return ruta_absoluta