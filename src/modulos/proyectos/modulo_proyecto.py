from datetime import datetime
from src.misc.metodos_validacion import validar_texto, validar_fecha
from src.misc.metodos_visualizacion import limpiar_consola, mostrar_proyectos, mostrar_equipos
from src.tablas.proyecto.metodos_proyecto import crear_proyecto, obtener_proyectos, modificar_proyecto, eliminar_proyecto, obtener_proyectos_por_equipo
from src.tablas.equipo.metodos_equipo import obtener_equipos
from src.misc.metodos_uuid import generar_uuid

def menu_proyectos(usuario):
    limpiar_consola()
    while True:
        print("Menú de proyectos")
        print("1. Mis proyectos")
        print("2. Todos los proyectos")
        print("3. Crear nuevo proyecto")
        print("4. Editar proyecto")
        print("5. Eliminar proyecto")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Proyectos: ")
            proyectos = obtener_proyectos_por_equipo(usuario["uuid_equipo"])
            mostrar_proyectos(proyectos)
        elif opcion == "2":
            print("Proyectos: ")
            proyectos = obtener_proyectos()
            mostrar_proyectos(proyectos)
        elif opcion == "3":
            uuid_proyecto = generar_uuid()
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            nombre_proyecto, end_date, uuid_equipo_seleccionado = obtener_datos_proyecto(usuario)

            proyecto = {
                "uuid": uuid_proyecto,
                "nombre": nombre_proyecto,
                "uuid_equipo": uuid_equipo_seleccionado,
                "end_date": end_date,
                "created_at": created_at,
                "deleted_at": None
            }

            crear_proyecto(proyecto)
        elif opcion == "4":
            proyectos = obtener_proyectos()
            print("Proyectos: ")
            mostrar_proyectos(proyectos)

            eleccion = int(input("Seleccione el número de proyecto que desea elegir: "))

            if 1 <= eleccion <= len(proyectos):
                proyecto_a_editar = proyectos[eleccion - 1]
                print("Editando proyecto")
                
                uuid_proyecto = proyecto_a_editar["uuid"]
                created_at = proyecto_a_editar["created_at"]
                deleted_at = proyecto_a_editar["deleted_at"]
                nombre_proyecto, end_date, uuid_equipo_seleccionado = obtener_datos_proyecto(usuario)

                proyecto_a_editar = {
                    "uuid": uuid_proyecto,
                    "nombre": nombre_proyecto,
                    "uuid_equipo": uuid_equipo_seleccionado,
                    "created_at": created_at,
                    "end_date": end_date,
                    "deleted_at": deleted_at
                }

                modificar_proyecto(proyecto_a_editar)
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(proyectos)}.")
        elif opcion == "5":
            # Llamar a la función para eliminar un proyecto
            proyectos = obtener_proyectos()
            print("Proyectos: ")
            mostrar_proyectos(proyectos)

            eleccion = int(input("Seleccione el número de proyecto que desea elegir: "))
            if 1 <= eleccion <= len(proyectos):
                proyecto_a_eliminar = proyectos[eleccion - 1]
                eliminar_proyecto(proyecto_a_eliminar)
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(proyectos)}.")
        elif opcion == "6":
            print("Volviendo")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_proyecto(usuario):
    """
        Obtiene los datos necesarios para crear un proyecto.
        Retorna un set con los elementos introducidos.
    """

    nombre_proyecto = input("Ingresar nombre del proyecto: ")

    while (not validar_texto(nombre_proyecto, "nombre")):
        nombre_proyecto = input("Ingresar nombre del proyecto: ")
    
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    uuid_equipo_seleccionado = None

    while not uuid_equipo_seleccionado:
        add_equipo = input("Desea agregar un equipo? (s/n):").strip().lower()

        if add_equipo == 's':
            equipos = obtener_equipos()
            print("Equipos: ")
            mostrar_equipos(equipos)

            numero_equipo = int(input("Seleccione el número de equipo que desea elegir: "))

            if 1 <= numero_equipo and numero_equipo <= len(equipos):
                equipo_seleccionado = equipos[numero_equipo - 1]
                uuid_equipo_seleccionado = equipo_seleccionado["uuid"]

        elif add_equipo == 'n':
            print("No se seleccionó ningún equipo.")
            break
        else:
            print("Opción inválida. Debe ingresar 's' o 'n'.")    
    
    return nombre_proyecto, end_date, uuid_equipo_seleccionado