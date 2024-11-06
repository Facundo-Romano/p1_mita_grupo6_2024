import pytest
from src.misc.metodos_os import obtener_ruta
from src.tablas.tarea import metodos_tarea

@pytest.fixture(autouse=True)
def set_ruta_absoluta_de_test(monkeypatch):
    ruta_test = obtener_ruta('tareas.json', 'test')
    monkeypatch.setattr(metodos_tarea, 'RUTA_ABSOLUTA_TAREAS', ruta_test)

TAREA_DE_PRUEBA_1 = {
        "uuid": "a405e61d-d971-4f72-903f-8758e12baa2e",
        "nombre": "Tarea de prueba 1",
        "created_at": "2021-01-01T00:00:00.000Z",
        "deleted_at": None,
}

TAREA_DE_PRUEBA_2 = {
        "uuid": "ae054623-3338-4b07-8d6a-5df2f0d801d5",
        "nombre": "Tarea de prueba 2",
        "created_at": "2022-01-01T00:00:00.000Z",
        "deleted_at": None,
}

TAREA_DE_PRUEBA_3 = {
        "uuid": "5988d299-8407-45f7-acfa-c74d5c04e401",
        "nombre": "Tarea de prueba 3",
        "created_at": "2023-01-01T00:00:00.000Z",
        "deleted_at": None,
}

def test_crear_tarea():
    assert metodos_tarea.crear_tarea(TAREA_DE_PRUEBA_1) == True
    assert metodos_tarea.crear_tarea(TAREA_DE_PRUEBA_2) == True
    assert metodos_tarea.crear_tarea(TAREA_DE_PRUEBA_3) == True

def test_obtener_tareas():
    assert metodos_tarea.obtener_tareas() == [TAREA_DE_PRUEBA_1, TAREA_DE_PRUEBA_2, TAREA_DE_PRUEBA_3]

def test_obtener_tarea():
    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_1["uuid"]) == TAREA_DE_PRUEBA_1
    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_2["uuid"]) == TAREA_DE_PRUEBA_2
    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_3["uuid"]) == TAREA_DE_PRUEBA_3

def test_modificar_tarea():
    TAREA_DE_PRUEBA_1["nombre"] = "tarea de prueba 1 modificado"
    assert metodos_tarea.modificar_tarea(TAREA_DE_PRUEBA_1) == True

    TAREA_DE_PRUEBA_2["nombre"] = "tarea de prueba 2 modificado"
    assert metodos_tarea.modificar_tarea(TAREA_DE_PRUEBA_2) == True

    TAREA_DE_PRUEBA_3["nombre"] = "tarea de prueba 3 modificado"
    assert metodos_tarea.modificar_tarea(TAREA_DE_PRUEBA_3) == True

    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_1["uuid"])["nombre"] == "tarea de prueba 1 modificado"
    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_2["uuid"])["nombre"] == "tarea de prueba 2 modificado"
    assert metodos_tarea.obtener_tarea(TAREA_DE_PRUEBA_3["uuid"])["nombre"] == "tarea de prueba 3 modificado"

def test_eliminar_tarea():
    assert metodos_tarea.eliminar_tarea(TAREA_DE_PRUEBA_1["uuid"]) == True
    assert metodos_tarea.eliminar_tarea(TAREA_DE_PRUEBA_2["uuid"]) == True
    assert metodos_tarea.eliminar_tarea(TAREA_DE_PRUEBA_3["uuid"]) == True

    assert metodos_tarea.obtener_tareas() == []
