import pytest
from src.misc.metodos_os import obtener_ruta
from src.tablas.equipo import metodos_equipo

@pytest.fixture(autouse=True)
def set_ruta_absoluta_de_test(monkeypatch):
    ruta_test = obtener_ruta('equipos.json', 'test')
    monkeypatch.setattr(metodos_equipo, 'RUTA_ABSOLUTA_EQUIPOS', ruta_test)

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
    assert metodos_equipo.crear_equipo(EQUIPO_DE_PRUEBA_1) == True
    assert metodos_equipo.crear_equipo(EQUIPO_DE_PRUEBA_2) == True
    assert metodos_equipo.crear_equipo(EQUIPO_DE_PRUEBA_3) == True

def test_obtener_equipos():
    assert metodos_equipo.obtener_equipos() == [EQUIPO_DE_PRUEBA_1, EQUIPO_DE_PRUEBA_2, EQUIPO_DE_PRUEBA_3]

def test_obtener_equipo():
    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_1["uuid"]) == EQUIPO_DE_PRUEBA_1
    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_2["uuid"]) == EQUIPO_DE_PRUEBA_2
    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_3["uuid"]) == EQUIPO_DE_PRUEBA_3

def test_modificar_equipo():
    EQUIPO_DE_PRUEBA_1["nombre"] = "Equipo de prueba 1 modificado"
    assert metodos_equipo.modificar_equipo(EQUIPO_DE_PRUEBA_1) == True

    EQUIPO_DE_PRUEBA_2["nombre"] = "Equipo de prueba 2 modificado"
    assert metodos_equipo.modificar_equipo(EQUIPO_DE_PRUEBA_2) == True

    EQUIPO_DE_PRUEBA_3["nombre"] = "Equipo de prueba 3 modificado"
    assert metodos_equipo.modificar_equipo(EQUIPO_DE_PRUEBA_3) == True

    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_1["uuid"])["nombre"] == "Equipo de prueba 1 modificado"
    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_2["uuid"])["nombre"] == "Equipo de prueba 2 modificado"
    assert metodos_equipo.obtener_equipo(EQUIPO_DE_PRUEBA_3["uuid"])["nombre"] == "Equipo de prueba 3 modificado"

def test_eliminar_equipo():
    assert metodos_equipo.eliminar_equipo(EQUIPO_DE_PRUEBA_1["uuid"]) == True
    assert metodos_equipo.eliminar_equipo(EQUIPO_DE_PRUEBA_2["uuid"]) == True
    assert metodos_equipo.eliminar_equipo(EQUIPO_DE_PRUEBA_3["uuid"]) == True

    assert metodos_equipo.obtener_equipos() == []
