import random

# Definir listas de estudiantes y materias
estudiantes = ["Ana", "Juan", "María", "Pedro", "Lucía"]
materias = ["Matemáticas", "Física", "Química", "Historia", "Literatura"]

# Crear e inicializar la matriz de calificaciones con valores aleatorios entre 1 y 10
def inicializar_matriz(estudiantes, materias):
    matriz = []
    for _ in estudiantes:
        fila = [random.randint(1, 10) for _ in materias]
        matriz.append(fila)
    return matriz

# Mostrar la matriz de calificaciones con encabezados
def mostrar_matriz(matriz, estudiantes, materias):
    print(" " * 12 + " ".join(f"{materia:<12}" for materia in materias))
    for i, estudiante in enumerate(estudiantes):
        calificaciones = " ".join(f"{nota:<12}" for nota in matriz[i])
        print(f"{estudiante:<12} {calificaciones}")

# Calcular y mostrar el promedio de calificaciones por estudiante
def calcular_promedio_estudiantes(matriz, estudiantes):
    print("\nPromedio por estudiante:")
    for i, estudiante in enumerate(estudiantes):
        promedio = sum(matriz[i]) / len(matriz[i])
        print(f"{estudiante:<12}: {promedio:.2f}")

# Calcular y mostrar el promedio de calificaciones por materia
def calcular_promedio_materias(matriz, materias):
    print("\nPromedio por materia:")
    for j, materia in enumerate(materias):
        suma_materia = sum(matriz[i][j] for i in range(len(matriz)))
        promedio = suma_materia / len(matriz)
        print(f"{materia:<12}: {promedio:.2f}")

# Ejecución del programa
matriz_calificaciones = inicializar_matriz(estudiantes, materias)

mostrar_matriz(matriz_calificaciones, estudiantes, materias)

calcular_promedio_estudiantes(matriz_calificaciones, estudiantes)

calcular_promedio_materias(matriz_calificaciones, materias)
