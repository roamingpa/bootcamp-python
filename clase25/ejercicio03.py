# Ejercicio 3 - Clase 25: introduccion a sys.argv
# Enunciado: crea un programa que reciba el nombre y la edad del usuario
#             por linea de comandos (sys.argv) y los imprima.
#             Si no se ingresan los argumentos, muestra un mensaje de error.
#
# Uso: python ejercicio03.py Ana 25
# Output esperado: Hola Ana, tienes 25 anios.
#
# Si falta un argumento:
# Output esperado: Error: debes ingresar nombre y edad. Uso: python ejercicio03.py <nombre> <edad>

import sys

if len(sys.argv) < 3:
    pass  # reemplaza con el mensaje de error
else:
    pass  # reemplaza con el codigo correcto
