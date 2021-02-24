def enviar_usuarios(func):
    def wrapper(usuarios):
        if type(usuarios) == list:
            for usuario in usuarios:
                func(usuario)
        else:
            return func(usuario)
    return wrapper