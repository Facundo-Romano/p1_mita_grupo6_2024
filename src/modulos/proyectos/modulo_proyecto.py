from src.misc.metodos_validacion import validar_texto, validar_fecha
from src.misc.metodos_visualizacion import limpiar_consola, mostrar_proyectos, mostrar_equipos
from src.tablas.proyecto.metodos_proyecto import crear_proyecto, obtener_proyectos, modificar_proyecto, eliminar_proyecto, obtener_proyectos_por_usuario
from src.tablas.equipo.metodos_equipo import obtener_equipos

def menu_proyectos(usuario):
    limpiar_consola()
    while True:
        print("Menú de proyectos")
        print("1. Mis proyectos")
        print("2. Crear nuevo proyecto")
        print("3. Editar proyecto")
        print("4. Eliminar proyecto")
        print("5. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Llamar a la función para obtener todos los proyectos
            proyectos = obtener_proyectos_por_usuario(usuario["uuid_equipo"])
            mostrar_proyectos(proyectos)
        elif opcion == "2":
            # Llamar a la función para crear tarea
            nombre_proyecto, end_date, uuid_equipo_seleccionado = obtener_datos_proyecto(usuario)

            crear_proyecto(nombre_proyecto, end_date, uuid_equipo_seleccionado)
        elif opcion == "3":
            # Llamar a la función para modificar un proyecto dado el uuid
            proyectos = obtener_proyectos()
            print("Proyectos: ")
            mostrar_proyectos(proyectos)

            eleccion = int(input("Seleccione el número de proyecto que desea elegir: "))
            if 1 <= eleccion <= len(proyectos):
                proyecto_a_editar = proyectos[eleccion - 1]
                print(f"Editando proyecto:{proyecto_a_editar['nombre']}")
                uuid_proyecto = proyecto_a_editar["uuid"]
                nombre_proyecto, end_date, uuid_equipo_seleccionado = obtener_datos_proyecto(usuario)
                created_at = proyecto_a_editar["created_at"]
                deleted_at = proyecto_a_editar["deleted_at"]
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

        elif opcion == "4":
            # Llamar a la función para eliminar un proyecto
            proyectos = obtener_proyectos()
            print("Proyectos: ")
            mostrar_proyectos(proyectos)

            eleccion = int(input("Seleccione el número de proyecto que desea eliminar: "))
            if 1 <= eleccion <= len(proyectos):
                proyecto_a_eliminar = proyectos[eleccion - 1]
                eliminar_proyecto(proyecto_a_eliminar)
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(proyectos)}.")

        elif opcion == "5":
            print("Volviendo")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def obtener_datos_proyecto(usuario):

    # Ver que pedir con Usuario
    """
    Obtiene los datos necesarios para crear un proyecto.
    Retorna una lista con los elementos introducidos.
    """

    nombre_proyecto = input("Ingresar nombre del proyecto: ")

    while (not validar_texto(nombre_proyecto, "nombre")):
        nombre_proyecto = input("Ingresar nombre del proyecto: ")
    
    end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    while validar_fecha(end_date) == False:
        end_date = input("Ingrese fecha finalizacion proyecto (dd-mm-yyyy): ")

    uuid_equipo_seleccionado = None
    while True:
        add_equipo = input("Desea agregar un equipo?(s/n):").strip().lower()
        if add_equipo == 's':
            equipos = obtener_equipos()
            print("Equipos: ")
            mostrar_equipos(equipos)

            uuid_equipo_seleccionado = elegir_equipo(equipos)
            if uuid_equipo_seleccionado:
                break
            else:
                print("Volviendo")
        
        elif add_equipo == 'n':
            print("No se seleccionó ningún equipo.")
            break
        else:
            print("Opción inválida. Debe ingresar 's' o 'n'.")    
    #Fin while

    return nombre_proyecto, end_date, uuid_equipo_seleccionado

def elegir_equipo(equipos):
    while True:
        try:
            eleccion = int(input("Seleccione el número del equipo que desea elegir(-1 para volver): "))
            if 1 <= eleccion <= len(equipos):
                equipo_seleccionado = equipos[eleccion - 1]
                return equipo_seleccionado["uuid"]
            elif eleccion == -1:
                return None
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(equipos)}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")