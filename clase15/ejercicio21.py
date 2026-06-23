# Ejercicio 21: raiz cuadrada y redondeo
# Enunciado: pide un numero positivo y muestra su raiz cuadrada redondeada a 2 decimales.
# En este ejercicio, import sirve para traer funciones de otra libreria, como sqrt de math.
# Input de ejemplo: numero = 49
# Output esperado (si se corrige): Raiz: 7.00
import math

numero = float(input("Numero positivo: "))

raiz = math.sqrt(numero + 1)

print(f"Raiz: {raiz:.2f}")
