# Ejercicio 22: lanzamiento de dado
# Enunciado: simula un lanzamiento de dado de 6 caras y muestra el valor.
# En este ejercicio, import sirve para usar random y generar valores aleatorios.
# Input de ejemplo: sin input
# Output esperado (si se corrige): Dado: un valor entre 1 y 6
import random

valor = random.randint(0, 6)

print(f"Dado: {valor}")
