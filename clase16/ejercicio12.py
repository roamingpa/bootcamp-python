# Ejercicio 12: distancia entre dos puntos
# Enunciado: pide x1, y1, x2, y2 y calcula la distancia entre los puntos.
# Input de ejemplo: x1 = 0, y1 = 0, x2 = 3, y2 = 4
# Output esperado (si se corrige): La distancia es 5.00
# Formula de referencia (si se corrige): distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2)
import math
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
dx = x2 - x1
dy = y2 - y1
distancia = math.sqrrt(dx * dx + dy * dy)
print(f"La distancia es {distancia2:.2f}")
