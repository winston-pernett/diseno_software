from decorators import enviar_usuarios

@enviar_usuarios
def enviar_mensaje(usuarios):
    return "Hola"

users = ["jules", "fred"]

print(enviar_mensaje(users))