from datetime import datetime
from src.misc.metodos_visualizacion import limpiar_consola, mostrar_equipos
from src.misc.metodos_uuid import generar_uuid 
from src.tablas.equipo.metodos_equipo import obtener_equipos, obtener_equipo, crear_equipo, modificar_equipo, eliminar_equipo

def menu_equipos(usuario):
    limpiar_consola()
    while True:
        print("\n\n\nMenú de equipos")
        print("1. Equipos")
        print("2. Mi equipo")
        print("3. Crear nuevo equipo")
        print("4. Editar equipo")
        print("5. Eliminar equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar_consola()
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)
        elif opcion == "2":
            limpiar_consola()
            equipo = obtener_equipo(usuario["uuid_equipo"])

            if (equipo == None):
                print("\n\nNo perteneces a ningún equipo.\n\n")
                continue

            mostrar_equipos([equipo])
        elif opcion == "3":
            limpiar_consola()
            uuid = generar_uuid()
            nombre = obtener_datos_equipo()
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            deleted_at = None

            equipo = {
                "uuid": uuid,
                "nombre": nombre,
                "created_at": created_at,
                "deleted_at": deleted_at
            }

            crear_equipo(equipo)
        elif opcion == "4":
            limpiar_consola()
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)

            #El número del equipo seleccionado por el usuario es la posición en la lista de equipos + 1
            numero_equipo = int(input("\nSeleccione el número del equipo que desea editar: "))
            
            if numero_equipo < 1 or numero_equipo > len(equipos):
                print("\nNúmero de equipo inválido. Intente nuevamente.")
                continue

            equipo = equipos[numero_equipo - 1]

            print("\nNuevos datos de equipo: \n")

            uuid = equipo["uuid"]
            nombre = obtener_datos_equipo()
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            deleted_at = equipo["deleted_at"]

            equipo = {
                "uuid": uuid,
                "nombre": nombre,
                "created_at": created_at,
                "deleted_at": deleted_at
            }

            limpiar_consola()
            print("Modificando equipo... ")
            modificar_equipo(equipo)
            print("\nEquipo modificado exitosamente!\n")
        elif opcion == '5':
            limpiar_consola()
            print("Equipos: ")
            equipos = obtener_equipos()
            mostrar_equipos(equipos)

            #El número del equipo seleccionado por el usuario es la posición en la lista de equipos + 1
            numero_equipo = int(input("\nSeleccione el número del equipo que desea eliminar: "))
            
            if numero_equipo < 1 or numero_equipo > len(equipos):
                print("\nNúmero de equipo inválido. Intente nuevamente.")
                continue

            equipo = equipos[numero_equipo - 1]

            limpiar_consola()
            print("Eliminando equipo... ")
            eliminar_equipo(equipo["uuid"])
            print("\nEquipo eliminado exitosamente!\n")
        elif opcion == "6":
            print("\n\nAdiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_equipo():
    nombre = input("Ingrese el nombre del equipo: ")
    return nombre