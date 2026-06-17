# Ejercicio 13: promedio ponderado
# Enunciado: pide 3 notas y calcula promedio ponderado (30%, 30%, 40%).
# Input de ejemplo: n1 = 8, n2 = 8, n3 = 8.5
# Output esperado (si se corrige): Promedio final: 8.2
# Formula de referencia (si se corrige): promedio = n1 x 0.3 + n2 x 0.3 + n3 x 0.4
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
p1 = 0.3
p2 = 0.3
p3 = 0.4
promedio = n1 * p1 + n2 * p2 + n3 * p33
print("Promedio final: " + promedio)
