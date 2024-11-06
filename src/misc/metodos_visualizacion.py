import os

def limpiar_consola():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux y macOS
        os.system('clear')

def mostrar_usuario_matriz(usuario):
    # Imprimir encabezados
    print(f"{'Nombre':<15} {'Apellido':<15} {'Email':<20}")
    print("=" * 50)  # Línea de separación

    # Imprimir cada tarea
    print(f"{usuario['nombre']:<15} {usuario['apellido']:<15} {usuario['mail']:<20}")
        
def mostrar_tareas_matriz(tareas):
    if not tareas:  # Si la lista de tareas está vacía
        print("No hay tareas para mostrar.")
        return

    # Imprimir encabezados
    print(f"{'UUID':<25} {'Título':<15} {'Descripción':<20} {'UUID Usuario':<15} {'UUID Proyecto':<25} {'Fecha de Creación':<25} {'Fecha de Fin':<25}")
    print("=" * 150)  # Línea de separación

    # Imprimir cada tarea
    for tarea in tareas:
        print(f"{tarea['uuid']:<25} {tarea['titulo']:<15} {tarea['descripcion']:<20} {tarea['uuid_usuario']:<15} {tarea['uuid_proyecto']:<25} {tarea['created_at']:<25} {tarea['end_date']:<15}")

def mostrar_tareas(tareas):
    for tarea in tareas:
        print()
        print(f"UUID: {tarea['uuid']}, Título: {tarea['titulo']}, Descripción: {tarea['descripcion']}, "
      f"UUID Usuario: {tarea['uuid_usuario']}, UUID Proyecto: {tarea['uuid_proyecto']}, "
      f"Fecha de Creación: {tarea['created_at']}, Fecha de Fin: {tarea['end_date']}")
        print()  # Salto de línea para separar cada tarea

def mostrar_equipos(equipos):
    for i in range(len(equipos)):
        print()
        print(f"{i+1}. Nombre: {equipos[i]['nombre']}, Fecha de Creación: {equipos[i]['created_at']}")
        print()

def mostrar_proyectos(proyectos):
    for index, proyecto in enumerate(proyectos, start = 1):
        print(f"{index}. Nombre: {proyecto['nombre']}, Creado: {proyecto['created_at']}, Finaliza: {proyecto['end_date']}")
        print()

visualizar_matriz = lambda matrix: print("\n".join([" | ".join([str(element) for element in row]) for row in matrix]))
#Convierte cada elemento de una fila en una cadena de texto.
#Une los elementos de la fila en una sola cadena, separándolos por |.
#Une todas las filas en una cadena de texto, separando cada fila con un salto de línea.