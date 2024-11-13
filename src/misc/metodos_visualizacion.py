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

def mostrar_equipos(equipos):
    print('\n')

    LONG_NUMERO = 5
    LONG_NOMBRE = 25
    LONG_CREACION = 25

    if not equipos:  # Si la lista de equipos está vacía
        print("No hay equipos para mostrar.")
        return

    # Imprimir encabezados
    print(f"{'Nro.':<{LONG_NUMERO}}{'Nombre':<{LONG_NOMBRE}}{'Creación':<{LONG_CREACION}}")

    # Línea de separación
    print("=" * (LONG_NUMERO + LONG_NOMBRE + LONG_CREACION))

    for i, equipo in enumerate(equipos):
            nombre = equipo['nombre'][:LONG_NOMBRE - 4] + '... ' if len(equipo['nombre']) >= LONG_NOMBRE else equipo['nombre']
            created_at = equipo['created_at'][:LONG_CREACION]

            print(f"{(str(i+1) + '.'):<{LONG_NUMERO}}"
                f"{nombre:<{LONG_NOMBRE}}"
                f"{created_at:<{LONG_CREACION}}")
    print()        
    
def mostrar_tareas(tareas):
    print('\n')

    LONG_NUMERO = 5
    LONG_TITULO = 25
    LONG_DESCRIPCION = 30
    LONG_CREACION = 25
    LONG_FINALIZACION = 15

    if not tareas:  # Si la lista de tareas está vacía
        print("No hay tareas para mostrar.")
        return

    # Imprimir encabezados
    print(f"{'Nro.':<{LONG_NUMERO}}{'Título':<{LONG_TITULO}}{'Descripción':<{LONG_DESCRIPCION}}{'Creación':<{LONG_CREACION}}{'Finalización':<{LONG_FINALIZACION}}")

    # Línea de separación
    print("=" * (LONG_NUMERO + LONG_TITULO + LONG_DESCRIPCION + LONG_CREACION + LONG_FINALIZACION))

    for i, tarea in enumerate(tareas):
            titulo = tarea['titulo'][:LONG_TITULO - 4] + '... ' if len(tarea['titulo']) >= LONG_TITULO else tarea['titulo']
            descripcion = tarea['descripcion'][:LONG_DESCRIPCION - 4] + '... ' if len(tarea['descripcion']) >= LONG_DESCRIPCION else tarea['descripcion']
            created_at = tarea['created_at'][:LONG_CREACION]
            end_date = tarea['end_date'][:LONG_FINALIZACION]

            print(f"{(str(i+1) + '.'):<{LONG_NUMERO}}"
                f"{titulo:<{LONG_TITULO}}"
                f"{descripcion:<{LONG_DESCRIPCION}}"
                f"{created_at:<{LONG_CREACION}}"
                f"{end_date:<{LONG_FINALIZACION}}")

def mostrar_subtarea(tarea, nivel = 0):
    subtarea = tarea['subtarea']
    if subtarea:
        print(f"{' ' * nivel * 4}Subtarea: {subtarea['nombre']} - Descripción: {subtarea['descripcion']}")
        mostrar_subtarea(subtarea, nivel + 1)

def mostrar_detalle_tarea(tarea, proyecto):
    print('\nTarea: \n')
    print(f"Título: {tarea['titulo']}")
    print(f"Descripción: {tarea['descripcion']}")
    print(f"Proyecto: {proyecto['nombre']}")
    print(f"Fecha de Creación: {tarea['created_at']}")
    print(f"Fecha de Finalización: {tarea['end_date']}")
    mostrar_subtarea(tarea)

def mostrar_proyectos(proyectos):
    print()
    print("Proyectos: ")

    LONG_NUMERO = 5
    LONG_NOMBRE = 25
    LONG_CREACION = 20
    LONG_FINALIZACION = 15

    if not proyectos:  # Si la lista de proyectos del usuario está vacía
            print("No está asignado a ningún proyecto.")
            return

    # Imprimir encabezados
    print(f"{'N°':<{LONG_NUMERO}}{'Nombre Proyecto':<{LONG_NOMBRE}}{'Fecha de Creación':<{LONG_CREACION}}{'Fecha de Fin':<{LONG_FINALIZACION}}")

    # Línea de Separación
    print("=" * (LONG_NUMERO + LONG_NOMBRE + LONG_CREACION + LONG_FINALIZACION))

    # Formateamos cada Proyectos
    for index, proyecto in enumerate(proyectos, start=1):
        nombre = proyecto['nombre'][:LONG_NOMBRE - 4] + '...' if len(proyecto['nombre']) >= LONG_NOMBRE else proyecto['nombre']
        fecha_creacion = proyecto['created_at'].split(" ")[0]  # Tomar solo la fecha
        print(f"{index:<3}{proyecto['nombre']:<25}{fecha_creacion:<20}{proyecto['end_date']:<20}")

visualizar_matriz = lambda matrix: print("\n".join([" | ".join([str(element) for element in row]) for row in matrix]))
#Convierte cada elemento de una fila en una cadena de texto.
#Une los elementos de la fila en una sola cadena, separándolos por |.
#Une todas las filas en una cadena de texto, separando cada fila con un salto de línea.