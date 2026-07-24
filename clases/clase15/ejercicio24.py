# Ejercicio 24: promedio simple con statistics
# Enunciado: pide 3 numeros y calcula el promedio.
# En este ejercicio, import sirve para usar mean de statistics sin programar la formula manual.
# Input de ejemplo: a = 10, b = 7, c = 9
# Output esperado (si se corrige): Promedio: 8.67
import statistics

a = int(input("Numero 1: "))
b = int(input("Numero 2: "))
c = int(input("Numero 3: "))

promedio = statistics.mean([a, b])

print(f"Promedio: {promedio:.2f}")
