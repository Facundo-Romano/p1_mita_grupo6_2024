import datetime
from misc.metodos_visualizacion import limpiar_consola, mostrar_equipos
from misc.metodos_uuid import generar_uuid 
from tablas.equipo.metodos_equipo import obtener_equipos, obtener_equipo, crear_equipo, modificar_equipo, eliminar_equipo

def menu_equipos(usuario):
    limpiar_consola()
    while True:
        print("Menú de equipos")
        print("1. Equipos")
        print("2. Mi equipo")
        print("3. Crear nuevo equipo")
        print("4. Editar equipo")
        print("5. Eliminar equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)
        elif opcion == "2":
            equipo = obtener_equipo(usuario["uuid_equipo"])

            if (equipo == None):
                print("No perteneces a ningún equipo.")
                continue

            mostrar_equipos([equipo])
        elif opcion == "3":
            uuid = generar_uuid()
            nombre = obtener_datos_equipo()
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            deleted_at = None

            equipo = {
                uuid,
                nombre,
                created_at,
                deleted_at
            }

            crear_equipo(equipo)
        elif opcion == "4":
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)

            #El número del equipo seleccionado por el usuario es la posición en la lista de equipos + 1
            numero_equipo = int(input("Seleccione el número del equipo que desea editar: "))
            
            if numero_equipo < 1 or numero_equipo > len(equipos):
                print("Número de equipo inválido. Intente nuevamente.")
                continue

            equipo = equipos[numero_equipo - 1]

            print("Nuevos datos de equipo: \n")

            uuid = equipo["uuid"]
            nombre = obtener_datos_equipo()
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            deleted_at = input("Ingrese la fecha de eliminación del equipo: ")

            equipo = {
                uuid,
                nombre,
                created_at,
                deleted_at
            }

            modificar_equipo(equipo)
        elif opcion == '5':
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)

            #El número del equipo seleccionado por el usuario es la posición en la lista de equipos + 1
            numero_equipo = int(input("Seleccione el número del equipo que desea eliminar: "))
            
            if numero_equipo < 1 or numero_equipo > len(equipos):
                print("Número de equipo inválido. Intente nuevamente.")
                continue

            equipo = equipos[numero_equipo - 1]

            eliminar_equipo(equipo["uuid"])
        elif opcion == "6":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_equipo():
    nombre = input("Ingrese el nombre del equipo: ")
    return nombre