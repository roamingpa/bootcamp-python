"""
PYTHON COMPREHENSIONS:
ES UNA FORMA MUY DE PYTHON DE ESCRIBIR LOOPS

GENERAR LISTAS, SETS, DICCIONARIO, ETC ETC
"""

acumulador = []
for item in "1123444":
    resultado = int(item) **2
    acumulador.append(resultado)

lista = [item.upper() for item in "abc123dgf"]
print("Lista: " + str(lista))

lista = [int(item)**2 for item in "123112312"]
print("Lista int al cuadrado: " + str(lista))

tupla = (int(item)**2 for item in "123112312")
print("Tupla int al cuadrado: " + str(tupla))

set_1 = {int(item)**2 for item in "123112312"}
print("Set 1 al cuadrado: " + str(set_1))

diccionario = {item: int(item)**2 for item in "123112312"}
print("Diccionario al cuadrado: " + str(diccionario))

## FILTROS

lista = [int(item)**2 for item in "123112312" if int(item) > 2]
print("Lista filtrada: " + str(lista))