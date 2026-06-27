# Ejercicio 4 - Clase 27: las 3 formas de importar
# Enunciado: usando el modulo temperatura.py del ejercicio anterior, importalo
#             de las 3 formas distintas y llama las funciones de cada forma.
#
# Forma 1: import temperatura
#           -> temperatura.celsius_a_fahrenheit(0)
#
# Forma 2: import temperatura as temp
#           -> temp.celsius_a_fahrenheit(0)
#
# Forma 3: from temperatura import celsius_a_fahrenheit, fahrenheit_a_celsius
#           -> celsius_a_fahrenheit(0)
#
# Output esperado (para cada forma, mismo resultado):
# Forma 1 -> 0°C = 32.0°F
# Forma 2 -> 0°C = 32.0°F
# Forma 3 -> 0°C = 32.0°F

import temperatura
import temperatura as temp
from temperatura import celsius_a_fahrenheit

print("Forma 1 ->", temperatura.celsius_a_fahrenheit(0))
print("Forma 2 ->", temp.celsius_a_fahrenheit(0))
print("Forma 3 ->", celsius_a_fahrenheit(0))
