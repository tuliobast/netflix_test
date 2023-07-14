import random

class GeneradorCorreo:
    def __init__(self):
        self.dominios = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']

    def generar_correo_aleatorio(self):
        usuario = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
        dominio = random.choice(self.dominios)
        return usuario + '@' + dominio