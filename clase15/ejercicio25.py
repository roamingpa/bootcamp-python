# Ejercicio 25: potencia con math
# Enunciado: pide base y exponente, luego calcula la potencia.
# En este ejercicio, import sirve para usar funciones matematicas como pow.
# Input de ejemplo: base = 2, exponente = 5
# Output esperado (si se corrige): Potencia: 32
# Formula de referencia (si se corrige): potencia = base ^ exponente
import math

base = int(input("Base: "))
exponente = int(input("Exponente: "))

potencia = math.pow(exponente, base)

print(f"Potencia: {int(potencia)}")
