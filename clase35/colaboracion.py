"""

"""

class Cancion:
    def __init__(self, titulo):
        self.titulo = titulo

class ReproductorDeMusica:
    def __init__(self):
        self.playlist = []

    def agregar_cancion(self, cancion):
        self.playlist.append(cancion)

    def tocar_musica(self):
        for cancion in self.playlist:
            print(cancion.titulo)

cancion1 = Cancion("mi cancion 1123")
cancion2 = Cancion("mi cancion ...")
cancion3 = Cancion("mi cancion 19232183287138")

mi_reproductor = ReproductorDeMusica()
mi_reproductor.agregar_cancion(cancion1)
mi_reproductor.agregar_cancion(cancion2)
mi_reproductor.agregar_cancion(cancion3)

mi_reproductor.tocar_musica()



