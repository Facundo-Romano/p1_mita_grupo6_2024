def obtener_equipos():
    return 'equipos'

def obtener_equipo(id_equipo):
    equipo = [
        {
            'uuid': 'prueba1',
            'nombre': 'equipo1',
            'created_at': '2020-09-11 11:00:00',
            'deleted_at': None
        },
        {
            'uuid': 'prueba2',
            'nombre': 'equipo2',
            'created_at': '2020-09-11 11:00:00',
            'deleted_at': None
        }
    ]

    return equipo

def obtener_equipo_por_usuario(id_usuario):
    equipo = {
        'uuid': 'prueba1',
        'nombre': 'equipo1',
        'created_at': '2020-09-11 11:00:00',
        'deleted_at': None
    }
    
    return equipo