

class Audio:
    def __init__(self):
        self.calidad_audio = "DOLBY ..."
    
    def reproducir_audio(self):
        print("reproduciendo audio...")

class Video:
    def __init__(self):
        self.resolucion = "IMAX"
    
    def reproducir_video(self):
        print("reproduciendo video...")


#### mixin -> seguridad

class Pelicula(Audio, Video):
    def __init__(self, titulo):
        Audio.__init__(self)
        Video.__init__(self)
        self.titulo = titulo

    def iniciar_pelicula(self):
        print("EMPEZANDO LA PELICULA")
        print(self.titulo)

        self.reproducir_audio()
        self.reproducir_video()

Pelicula("Mi pelicula 123").iniciar_pelicula()