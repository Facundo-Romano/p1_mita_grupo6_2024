import os

def acceder_subtareas(tarea):
    # Imprimir la tarea actual
    print(f"Tarea: {tarea['titulo']} - UUID: {tarea['uuid']}")
    
    # Acceder a las subtareas recursivamente
    for subtarea in tarea.get('subtareas', []):
        acceder_subtareas(subtarea)  # Llamada recursiva para cada subtarea

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
    print(f"{'Título':<15} {'Descripción':<20} {'Fecha de Creación':<25} {'Fecha de Fin':<25}")
    print("=" * 75)  # Línea de separación

    # Imprimir cada tarea
    for tarea in tareas:
        print(f"{tarea['titulo']:<15} {tarea['descripcion']:<20} {tarea['created_at']:<25} {tarea['end_date']:<15}")


def mostrar_equipos(equipos):
    for i in range(len(equipos)):
        print()
        print(f"{i+1}. Nombre: {equipos[i]['nombre']}, Fecha de Creación: {equipos[i]['created_at']}")
        print()

def mostrar_proyectos(proyectos):
    if not proyectos:  # Si la lista de proyectos del usuario está vacía
            print("No está asignado a ningún proyecto.")
            return

    # Imprimir encabezados
    print(f"{'N°':<3}{'Nombre Proyecto':<25}{'Fecha de Creación':<20}{'Fecha de Fin':<15}")
    print("=" * 60)

    # Imprimir Proyectos
    for index, proyecto in enumerate(proyectos, start = 1):
        fecha_creacion = proyecto['created_at'].split(" ")[0]  # Tomar solo la fecha
        print(f"{index:<3}{proyecto['nombre']:<25}{fecha_creacion:<20}{proyecto['end_date']:<20}")

visualizar_matriz = lambda matrix: print("\n".join([" | ".join([str(element) for element in row]) for row in matrix]))
#Convierte cada elemento de una fila en una cadena de texto.
#Une los elementos de la fila en una sola cadena, separándolos por |.
#Une todas las filas en una cadena de texto, separando cada fila con un salto de línea.