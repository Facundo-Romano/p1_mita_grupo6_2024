import os

def obtener_ruta(archivo):
    directorio_actual = os.getcwd()
    ruta_absoluta = os.path.join(directorio_actual, 'assets', archivo)

    return ruta_absoluta