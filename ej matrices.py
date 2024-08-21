import random

# Paso 1: Inicialización de la matriz
estudiantes = ["Mario", "María", "Pedro", "Laura", "Oscar"]
materias = ["Matemáticas", "Historia", "Biología"]

matriz_calificaciones = []

for i in range(len(estudiantes)):
    calificaciones = []
    for j in range(len(materias)):
        calificacion = random.randint(1, 10)
        calificaciones.append(calificacion)
    matriz_calificaciones.append(calificaciones)

# Paso 2: Mostrar la matriz
def mostrar_matriz(matriz, estudiantes, materias):
    print("    |", end="")  # Espacio para alinear las materias con los nombres de los estudiantes
    for materia in materias:
        print(materia, end="|")  # Imprime el nombre de cada materia
    print()  # Salto de línea

    for i in range(len(estudiantes)):
        print(estudiantes[i], end="    ")  # Imprime el nombre del estudiante
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="          ")  # Imprime cada calificación con espacios para alinear
        print()  # Salto de línea

mostrar_matriz(matriz_calificaciones, estudiantes, materias)

# Paso 3: Calcular el promedio por estudiante
def calcular_promedio_estudiantes(matriz, estudiantes):
    print("\nPromedio de calificaciones por estudiante:")
    for i in range(len(estudiantes)):
        suma = sum(matriz[i])
        promedio = suma / len(matriz[i])
        print(estudiantes[i] + " tiene un promedio de " + str(promedio))

calcular_promedio_estudiantes(matriz_calificaciones, estudiantes)

# Paso 4: Calcular el promedio por materia
def calcular_promedio_materias(matriz, materias):
    print("\nPromedio de calificaciones por materia:")
    for j in range(len(materias)):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print(materias[j] + " tiene un promedio de " + str(promedio))

calcular_promedio_materias(matriz_calificaciones, materias)