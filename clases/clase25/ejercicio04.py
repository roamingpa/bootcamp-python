# Ejercicio 4 - Clase 25: PREPARACION DESAFIO I - Conversor de monedas
# Enunciado: practica del desafio evaluado. Crea un programa conversiones.py
#             que reciba por sys.argv las tasas de conversion y el monto en
#             pesos chilenos, y muestre el equivalente en cada moneda.
#
# Argumentos: tasa_sol tasa_peso_arg tasa_dolar monto_clp
# Uso: python ejercicio04.py 0.0046 0.093 0.00013 10000
#
# Output esperado:
# Los 10000 pesos equivalen a:
# 46.0 Soles
# 930.0 Pesos Argentinos
# 1.3 Dolares
#
# PISTA: usa un diccionario para asociar el nombre de la moneda con su tasa.
#        Recorre el diccionario con .items() para imprimir cada conversion.

import sys

if len(sys.argv) != 5:
    print("Uso: python ejercicio04.py <tasa_sol> <tasa_arg> <tasa_dolar> <monto>")
else:
    tasa_sol = float(sys.argv[1])
    tasa_arg = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    monto = float(sys.argv[4])

    tasas = {
        "Soles": tasa_sol,
        # agrega las otras dos monedas
    }

    # recorre el diccionario e imprime cada conversion
