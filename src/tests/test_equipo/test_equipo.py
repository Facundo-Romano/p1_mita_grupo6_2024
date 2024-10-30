from src.misc.metodos_os import obtener_ruta
from src.modulos.equipos import modulo_equipos

modulo_equipos.RUTA_ABSOLUTA_EQUIPOS = obtener_ruta('equipos.json', 'test')

EQUIPO_DE_PRUEBA_1 = {
        "uuid": "a405e61d-d971-4f72-903f-8758e12baa2e",
        "nombre": "Equipo de prueba 1",
        "created_at": "2021-01-01T00:00:00.000Z",
        "deleted_at": None,
}

EQUIPO_DE_PRUEBA_2 = {
        "uuid": "ae054623-3338-4b07-8d6a-5df2f0d801d5",
        "nombre": "Equipo de prueba 2",
        "created_at": "2022-01-01T00:00:00.000Z",
        "deleted_at": None,
}

EQUIPO_DE_PRUEBA_3 = {
        "uuid": "5988d299-8407-45f7-acfa-c74d5c04e401",
        "nombre": "Equipo de prueba 3",
        "created_at": "2023-01-01T00:00:00.000Z",
        "deleted_at": None,
}

def test_crear_equipo():
    assert modulo_equipos.crear_equipo(EQUIPO_DE_PRUEBA_1) == True
    assert modulo_equipos.crear_equipo(EQUIPO_DE_PRUEBA_2) == True
    assert modulo_equipos.crear_equipo(EQUIPO_DE_PRUEBA_3) == True

def test_obtener_equipos():
    assert modulo_equipos.obtener_equipos() == [EQUIPO_DE_PRUEBA_1, EQUIPO_DE_PRUEBA_2, EQUIPO_DE_PRUEBA_3]

def test_obtener_equipo():
    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_1["uuid"]) == EQUIPO_DE_PRUEBA_1
    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_2["uuid"]) == EQUIPO_DE_PRUEBA_2
    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_3["uuid"]) == EQUIPO_DE_PRUEBA_3

def test_modificar_equipo():
    EQUIPO_DE_PRUEBA_1["nombre"] = "Equipo de prueba 1 modificado"
    assert modulo_equipos.modificar_equipo(EQUIPO_DE_PRUEBA_1) == True

    EQUIPO_DE_PRUEBA_2["nombre"] = "Equipo de prueba 2 modificado"
    assert modulo_equipos.modificar_equipo(EQUIPO_DE_PRUEBA_2) == True

    EQUIPO_DE_PRUEBA_3["nombre"] = "Equipo de prueba 3 modificado"
    assert modulo_equipos.modificar_equipo(EQUIPO_DE_PRUEBA_3) == True

    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_1["uuid"])["nombre"] == "Equipo de prueba 1 modificado"
    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_2["uuid"])["nombre"] == "Equipo de prueba 2 modificado"
    assert modulo_equipos.obtener_equipo(EQUIPO_DE_PRUEBA_3["uuid"])["nombre"] == "Equipo de prueba 3 modificado"

def test_eliminar_equipo():
    assert modulo_equipos.eliminar_equipo(EQUIPO_DE_PRUEBA_1["uuid"]) == True
    assert modulo_equipos.eliminar_equipo(EQUIPO_DE_PRUEBA_2["uuid"]) == True
    assert modulo_equipos.eliminar_equipo(EQUIPO_DE_PRUEBA_3["uuid"]) == True

    assert modulo_equipos.obtener_equipos(EQUIPO_DE_PRUEBA_1["uuid"]) == []

modulo_equipos.RUTA_ABSOLUTA_EQUIPOS = obtener_ruta('equipos.json')