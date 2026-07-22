import random

class Personaje:
    # atributos estaticos
    # juego = "juego bonito"

    # métodos de instancia
    # sobrecargar
    # override
    def __init__(self, nombre):
        # atributos de instancia
        self.nombre = nombre
        self.experiencia = 0 
        self.nivel = 1

    # pj1 > pj2
    def __gt__(self, other):
        return self.nivel > other.nivel

    # pj1 < pj2
    def __lt__(self, other):
        return self.nivel < other.nivel

    # pj1 == pj2
    def __eq__(self, other):
        return self.nivel == other.nivel

    # pj1 >= pj2
    # mayor o igual
    def __ge__(self, other):
        return self.nivel >= other.nivel
    
    # pj1 <= pj2
    # menor o igual
    def __le__(self, other):
        return self.nivel <= other.nivel

    ### getter = obtener = leer
    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"
    
    ### setter = establecer = modificar
    @estado.setter
    def estado(self, experiencia):
        experiencia_temporal = self.experiencia + experiencia
        print(f"experiencia pre combate: {self.experiencia}")
        print(f"experiencia por combate: {experiencia}")
        print(f"experiencia temporal: {experiencia_temporal}")

        if experiencia != 0:
            total_experiencia = (self.nivel * 100) + self.experiencia
            total_experiencia = total_experiencia + experiencia
            nivel_post_combate = total_experiencia // 100 

            if nivel_post_combate < 1:
                self.nivel = 1
                self.experiencia = 0
            else:
                self.nivel = nivel_post_combate
                self.experiencia = experiencia_temporal % 100
        else:
            self.experiencia = experiencia_temporal

    def probabilidad_de_ganar(self, otro_personaje):
        probabilidad = 0.0
        if self == otro_personaje:
            probabilidad = 0.5
        elif self < otro_personaje:
            probabilidad = 0.33
        elif self > otro_personaje:
            probabilidad = 0.66
        return probabilidad

    def mostrar_dialogo_enfrentamiento(self, otro_personaje):
        dialogo = f"""\n
Con tu nivel actual, tienes {self.probabilidad_de_ganar(otro_personaje) * 100}% de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
¿Qué deseas hacer?
1. Atacar
2. Huir\n
        """
        return int(input(dialogo))


    def combatir(self, otro_personaje):
        numero_random = random.uniform(0, 1)
        probabilidad_de_ganar = self.probabilidad_de_ganar(otro_personaje)
        if numero_random <= probabilidad_de_ganar:
            # ganamos
            self.estado = 50
            otro_personaje.estado = -30
            print("¡Le has ganado al orco, felicidades! ¡Recibirás 50 puntos de experiencia!")
            print("")
        else:
            # perdimos
            self.estado = -30
            otro_personaje.estado = 50
            print("¡Oh no! ¡El orco te ha ganado! ¡Has perdido 30 puntos de experiencia!")
            print("")
