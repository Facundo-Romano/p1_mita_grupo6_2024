def mostrar_tareas(tareas):
    for tarea in tareas:
        print("Tareas")
        print(f"UUID: {tarea['uuid_prueba']}, Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, "
              f"UUID Usuario: {tarea['uuid_usuario']}, UUID Proyecto: {tarea['uuid_proyecto']}, "
              f"Fecha de Creación: {tarea['created_at']}, Fecha de Fin: {tarea['end_date']}")
        print()  # Salto de línea para separar cada tarea

visualizar_matriz = lambda matrix: print("\n".join([" | ".join([str(element) for element in row]) for row in matrix]))
