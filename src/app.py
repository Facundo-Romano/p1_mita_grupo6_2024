from tablas.usuario.metodos_usuario import crear_usuario

usuarios = [
    ['uuid', 'nombre', 'apellido', 'equipo', 'mail', 'contraseña', 'created_at'],
]

def init():
    usuario = crear_usuario()

    usuarios.append(list(usuario.values()))

    print(f'Usuarios: {usuarios}')




init()