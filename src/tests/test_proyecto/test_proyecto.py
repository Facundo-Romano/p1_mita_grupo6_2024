import pytest
from src.misc.metodos_os import obtener_ruta
from src.tablas.proyecto import metodos_proyecto

@pytest.fixture(autouse=True)
def set_ruta_absoluta_de_test(monkeypatch):
    ruta_test = obtener_ruta('proyectos.json', 'test')
    monkeypatch.setattr(metodos_proyecto, 'RUTA_ABSOLUTA_PROYECTOS', ruta_test)

PROYECTO_DE_PRUEBA_1 = {
        "uuid": "a405e61d-d971-4f72-903f-8758e12baa2e",
        "nombre": "Proyecto de prueba 1",
        "uuid_equipo": "962f264a-b27c-48d6-bf49-07bbffd19ee3",
        "end_date": "2022-01-01T00:00:00.000Z",
        "created_at": "2021-01-01T00:00:00.000Z",
        "deleted_at": None,
}

PROYECTO_DE_PRUEBA_2 = {
        "uuid": "ae054623-3338-4b07-8d6a-5df2f0d801d5",
        "nombre": "Proyecto de prueba 2",
        "uuid_equipo": "17a1d14d-f0fe-45a8-8a3a-8647241ab381",
        "end_date": "2023-01-01T00:00:00.000Z",
        "created_at": "2022-01-01T00:00:00.000Z",
        "deleted_at": None,
}

PROYECTO_DE_PRUEBA_3 = {
        "uuid": "5988d299-8407-45f7-acfa-c74d5c04e401",
        "nombre": "Proyecto de prueba 3",
        "uuid_equipo": "05667426-1bf3-4c2d-a71a-920f8b6d7334",
        "end_date": "2024-01-01T00:00:00.000Z",
        "created_at": "2023-01-01T00:00:00.000Z",
        "deleted_at": None,
}

def test_crear_proyecto():
    assert metodos_proyecto.crear_proyecto(PROYECTO_DE_PRUEBA_1) == True
    assert metodos_proyecto.crear_proyecto(PROYECTO_DE_PRUEBA_2) == True
    assert metodos_proyecto.crear_proyecto(PROYECTO_DE_PRUEBA_3) == True

def test_obtener_proyectos():
    assert metodos_proyecto.obtener_proyectos() == [PROYECTO_DE_PRUEBA_1, PROYECTO_DE_PRUEBA_2, PROYECTO_DE_PRUEBA_3]

def test_obtener_proyecto():
    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_1["uuid"]) == PROYECTO_DE_PRUEBA_1
    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_2["uuid"]) == PROYECTO_DE_PRUEBA_2
    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_3["uuid"]) == PROYECTO_DE_PRUEBA_3

def test_modificar_proyecto():
    PROYECTO_DE_PRUEBA_1["nombre"] = "proyecto de prueba 1 modificado"
    assert metodos_proyecto.modificar_proyecto(PROYECTO_DE_PRUEBA_1) == True

    PROYECTO_DE_PRUEBA_2["nombre"] = "proyecto de prueba 2 modificado"
    assert metodos_proyecto.modificar_proyecto(PROYECTO_DE_PRUEBA_2) == True

    PROYECTO_DE_PRUEBA_3["nombre"] = "proyecto de prueba 3 modificado"
    assert metodos_proyecto.modificar_proyecto(PROYECTO_DE_PRUEBA_3) == True

    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_1["uuid"])["nombre"] == "proyecto de prueba 1 modificado"
    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_2["uuid"])["nombre"] == "proyecto de prueba 2 modificado"
    assert metodos_proyecto.obtener_proyecto(PROYECTO_DE_PRUEBA_3["uuid"])["nombre"] == "proyecto de prueba 3 modificado"

def test_eliminar_proyecto():
    assert metodos_proyecto.eliminar_proyecto(PROYECTO_DE_PRUEBA_1["uuid"]) == True
    assert metodos_proyecto.eliminar_proyecto(PROYECTO_DE_PRUEBA_2["uuid"]) == True
    assert metodos_proyecto.eliminar_proyecto(PROYECTO_DE_PRUEBA_3["uuid"]) == True

    assert metodos_proyecto.obtener_proyectos() == []
