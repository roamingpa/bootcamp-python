"""
if = si condicional
if (condicion):
    # esto se va a ejecutar
    print(...)
"""
numero = 18
# int
# float
# str
# list
# set
# dict
# tupla (111, 1231,...)
# bool = verdadero o falso / si o no / true or false
numero_es_mayor_a_0 = numero > 0

print(type(numero_es_mayor_a_0))
print("Variable numero_es_mayor_a_0: " + str(numero_es_mayor_a_0))
if (numero_es_mayor_a_0):
    print(f"Si, {numero} es mayor a 0")

if (numero > 5 and numero < 7):
    print(f"Si, {numero} es mayor a 5 y menor a 7")

if (numero > 0 or numero == -1):
    print(f"Si, {numero} es mayor a 0 o numero es -1")
