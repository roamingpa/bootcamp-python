# Ejercicio 29: deteccion de outlier simple
# Enunciado: pide 5 valores y detecta si el ultimo esta a mas de 2 desviaciones del promedio.
# En este ejercicio, import sirve para usar mean y pstdev de statistics.
# Input de ejemplo: 10, 11, 10, 12, 35
# Output esperado (si se corrige): Outlier: Si
# Formula de referencia (si se corrige): z = abs(x - media) / desviacion
import statistics

valores = []
for i in range(5):
    v = float(input(f"Valor {i + 1}: "))
    valores.append(v)

media = statistics.mean(valores)
desv = statistics.pstdev(valores)
ultimo = valores[-1]

z = abs(ultimo - media) / desv

if z > 2:
    print("Outlier: No")
else:
    print("Outlier: Si")
