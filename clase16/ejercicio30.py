# Ejercicio 30: interes compuesto con log para estimar tiempo
# Enunciado: pide capital objetivo, capital inicial y tasa anual (%), y estima anios para alcanzar el objetivo.
# En este ejercicio, import sirve para usar logaritmos de math y resolver una ecuacion exponencial.
# Input de ejemplo: objetivo = 2000, inicial = 1000, tasa = 10
# Output esperado (si se corrige): Anios estimados: 8
# Formula de referencia (si se corrige): anios = log(objetivo / inicial) / log(1 + tasa / 100)
import math

objetivo = float(input("Capital objetivo: "))
inicial = float(input("Capital inicial: "))
tasa = float(input("Tasa anual (%): "))

anios = math.log(objetivo / inicial) / math.log(1 + tasa)

print(f"Anios estimados: {round(anios)}")
