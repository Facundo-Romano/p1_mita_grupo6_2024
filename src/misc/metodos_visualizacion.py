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
    # Encabezados para la tabla
    encabezados = ["N°", "Nombre", "Fecha de Creación"]
    
    # Mostrar la tabla con los equipos enumerados
    print("\n" + "-" * 60)
    print(f"{encabezados[0]:<5} {encabezados[1]:<25} {encabezados[2]:<25}")
    print("-" * 60)
    #Enumerate para mostrar el número de equipo y el start para que empiece por el 1
    for i, equipo in enumerate(equipos, start=1):
        print(f"{i:<5} {equipo['nombre']:<25} {equipo['created_at']:<25}")
    
    print("-" * 60)
     
    
def mostrar_tareas(tareas):
    print('\n')

    LONG_NUMERO = 5
    LONG_TITULO = 25
    LONG_DESCRIPCION = 30
    LONG_CREACION = 25
    LONG_FINALIZACION = 15

    if not tareas:  # Si la lista de tareas está vacía
        print("No hay tareas para mostrar.")
        return False

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
    # Convertir los proyectos a una matriz
    matriz_proyectos = []

    # Agregar encabezados
    encabezados = ["UUID", "Nombre", "Fecha de Creación", "Fecha de Finalización"]
    matriz_proyectos.append(encabezados)

    # Agregar cada proyecto a la matriz
    for proyecto in proyectos:
        fila_proyecto = [
            proyecto["nombre"],
            proyecto["created_at"],
            proyecto["end_date"]
        ]
        matriz_proyectos.append(fila_proyecto)

    # Mostrar la matriz de proyectos de forma ordenada
    print("\n" + "-" * 70)
    print(f"{'Nombre':<25} {'Fecha de Creación':<25} {'Fecha de Finalización':<20}")
    print("-" * 70)

    for fila in matriz_proyectos[1:]:  # Excluir encabezados
        print(f"{fila[0]:<25} {fila[1]:<25} {fila[2]:<20}")

    print("-" * 70)
