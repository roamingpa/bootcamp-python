# calcular distancia -> (punto inicio, punto fin)

# abstract class -> utilidades en python para trabajar las clases 
# abstractas
from abc import ABC, abstractmethod

class CalculadoraAbstracta(ABC):
    @abstractmethod
    def calcular_distancia(self, punto_inicio, punto_fin):
        pass


class CalculadoraManual(CalculadoraAbstracta):
    def calcular_distancia(self, punto_inicio, punto_fin):
        ...
        return ...

class CalculadoraGoogleMaps(CalculadoraAbstracta):
    def calcular_distancia(self, punto_inicio, punto_fin):
        # llamar al servicio de google maps
        return ...

class CalculadoraUber(CalculadoraAbstracta):
    def calcular_distancia(self, punto_inicio, punto_fin):
        # llamar al servicio de UBER
        return ...
    
class CalculadoraWaze(CalculadoraAbstracta):
    def calcular_distancia(self, punto_inicio, punto_fin):
        # llamar al servicio de WAZE
        return ...


...
punto_inicio = 0
punto_fin = 0
servicio_uber = True
servicio_google_maps = True
servicio_waze = True
# 

calculadora = CalculadoraManual()
if servicio_uber == True:
    calculadora = CalculadoraUber()
elif servicio_google_maps == True:
    calculadora = CalculadoraGoogleMaps()
elif servicio_waze == True:
    calculadora = CalculadoraWaze()

calculadora.calcular_distancia(punto_inicio=punto_inicio, punto_fin=punto_fin)


