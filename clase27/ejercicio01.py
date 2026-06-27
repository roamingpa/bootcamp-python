# Ejercicio 1 - Clase 27: agregar docstring a una funcion
# Enunciado: las siguientes funciones no tienen documentacion. Agrega un docstring
#             a cada una explicando: que hace, sus parametros y que retorna.
#             Usa el formato Google (Args / Returns).
# Despues de agregar los docstrings, verifica que aparecen al invocar help().

def calcular_descuento(precio, porcentaje):
    # agrega el docstring aqui
    return precio * (1 - porcentaje / 100)


def es_primo(numero):
    # agrega el docstring aqui
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# descomenta para verificar que el docstring aparece:
# help(calcular_descuento)
# help(es_primo)
print(calcular_descuento(10000, 15))
print(es_primo(7))
