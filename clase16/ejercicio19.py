# Ejercicio 19: area y perimetro de un circulo
# Enunciado: pide el radio y muestra area y perimetro.
# Input de ejemplo: radio = 5
# Output esperado (si se corrige): Area: 78.54 | Perimetro: 31.42
# Formula de referencia (si se corrige): area = pi * radio ** 2; perimetro = 2 * pi * radio
import math

radio = int(input("Radio: "))

area = 2 * math.pi * radio
perimetro = math.pi * (radio ^ 2)

print(f"Area: {area:.2f}")
print(f"Perimetro: {perimetro:.2f}")
