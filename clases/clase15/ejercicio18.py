# Ejercicio 18: promedio ponderado de curso
# Enunciado: pide 4 notas y calcula promedio con pesos 20%, 20%, 30%, 30%.
# Input de ejemplo: n1 = 9, n2 = 8, n3 = 7, n4 = 8
# Output esperado (si se corrige): Promedio final: 7.9
n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))
n4 = int(input("Nota 4: "))

p1 = 20
p2 = 20
p3 = 30
p4 = 30

promedio = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4) / 1000
promedio = int(promedio)

print(f"Promedio final: {promedio}")
