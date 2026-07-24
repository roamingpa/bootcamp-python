# Ejercicio 5 - Clase 27: mini proyecto modularizado
# Enunciado: organiza una calculadora basica en modulos separados.
#             La estructura del proyecto debe ser:
#
#   clase27/
#     main.py         <- archivo principal (este archivo)
#     operaciones.py  <- modulo con las funciones: sumar, restar, multiplicar, dividir
#
# Cada funcion en operaciones.py debe:
#   - tener su docstring
#   - recibir dos numeros y retornar el resultado
#   - dividir debe retornar None si el divisor es 0
#
# Este archivo (main.py) debe:
#   1) Importar las funciones desde operaciones.py
#   2) Mostrar un menu al usuario
#   3) Pedir dos numeros y llamar la funcion correspondiente
#
# Output esperado (si el usuario elige sumar, a=10, b=3):
# 1. Sumar  2. Restar  3. Multiplicar  4. Dividir
# Opcion: 1
# Numero A: 10
# Numero B: 3
# Resultado: 13
#
# INSTRUCCION: primero crea el archivo operaciones.py en esta carpeta,
#              luego completa el codigo de abajo.

# from operaciones import sumar, restar, multiplicar, dividir

opcion = input("1. Sumar  2. Restar  3. Multiplicar  4. Dividir\nOpcion: ")
a = float(input("Numero A: "))
b = float(input("Numero B: "))

# completa la logica del menu aqui
