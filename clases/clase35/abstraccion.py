from abc import ABC, abstractmethod

class PelotaAbstracta(ABC):
# No se tiene la lógica del método en la clase abstracta
    @abstractmethod
    def rebotar(self, altura: int):
        pass

class PelotasDeJuguete(PelotaAbstracta):
    def rebotar(self, altura: float):
        self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2


pelota_andy = PelotasDeJuguete()
pelota_andy.rebotar(10)