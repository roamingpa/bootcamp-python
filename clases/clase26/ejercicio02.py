# Ejercicio 2 - Clase 26: *args - cantidad variable de argumentos
# Enunciado: define una funcion suma_total(*args) que reciba cualquier cantidad
#             de numeros y retorne su suma. Llámala con 2, 4 y 0 argumentos.
# Output esperado:
# suma_total(3, 5)        -> 8
# suma_total(1, 2, 3, 4)  -> 10
# suma_total()            -> 0
#


def suma_total(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma



print(suma_total(3, 5))
print(suma_total(1, 2, 3, 4))
print(suma_total())


# BONUS: define tambien promedio(*args) que retorne el promedio,
#        o "Sin datos" si se llama sin argumentos.
def promedio(*args):
    if len(args) == 0:
        return "Sin datos"
    resultado = sum(args)/len(args)
    return resultado 

print(promedio(3, 5))
print(promedio(1, 2, 3, 4))
print(promedio())
