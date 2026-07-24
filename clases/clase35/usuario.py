class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    def contestar_encuesta(self):
        pass
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo


class Componente():
    ...

class Componente1():
    ...

class Componente2():
    ...


class Hija(Componente, Componente1, Componente2):
    ...



class Nieto(Hija):
    ...


class Nieta(Hija):
    ...
    
        