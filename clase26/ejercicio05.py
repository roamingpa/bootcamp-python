# Ejercicio 5 - Clase 26: PREPARACION DESAFIO II - Filtrar diccionario por umbral
# Enunciado: practica del desafio evaluado (filtro.py). Implementa una funcion
#             filtrar(diccionario, umbral, modo="mayor") que retorne un
#             diccionario con los productos que cumplen la condicion.
#             - modo="mayor": productos con precio ESTRICTAMENTE mayor al umbral
#             - modo="menor": productos con precio ESTRICTAMENTE menor al umbral
#             - cualquier otro modo: retorna None
#
# Luego el programa recibe el umbral y el modo por sys.argv e imprime el resultado.
#
# Uso: python ejercicio05.py 30000
#   -> Los productos mayores al umbral son: Notebook, Monitor, Escritorio, Tarjeta de Video
#
# Uso: python ejercicio05.py 30000 menor
#   -> Los productos menores al umbral son: Teclado, Mouse
#
# Uso: python ejercicio05.py 30000 otro
#   -> Lo sentimos, no es una operacion valida
#
# PISTA: usa .join() para mostrar los nombres separados por coma.

import sys

precios = {
    "Notebook": 700000, "Teclado": 25000, "Mouse": 12000,
    "Monitor": 250000, "Escritorio": 135000, "Tarjeta de Video": 1500000
}


def filtrar(diccionario, umbral, modo="mayor"):
    pass  # reemplaza con el codigo correcto


if len(sys.argv) < 2:
    print("Uso: python ejercicio05.py <umbral> [mayor|menor]")
else:
    umbral = int(sys.argv[1])
    modo = sys.argv[2] if len(sys.argv) == 3 else "mayor"
    # llama a filtrar() e imprime el resultado
