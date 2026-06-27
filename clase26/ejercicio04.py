# Ejercicio 4 - Clase 26: funcion como argumento
# Enunciado: define dos funciones: mayusculas(lista) y longitudes(lista).
#             Luego define aplicar(lista, funcion) que recibe una lista y una
#             funcion, la aplica sobre la lista y retorna el resultado.
#             Llámala pasando cada funcion como argumento.
# Input de ejemplo: palabras = ["hola", "mundo", "python"]
# Output esperado:
# Mayusculas: ['HOLA', 'MUNDO', 'PYTHON']
# Longitudes: [4, 5, 6]

def mayusculas(lista):
    pass  # retorna lista con cada elemento en mayusculas


def longitudes(lista):
    pass  # retorna lista con la longitud de cada elemento


def aplicar(lista, funcion):
    pass  # aplica la funcion y retorna el resultado


palabras = ["hola", "mundo", "python"]
print("Mayusculas:", aplicar(palabras, mayusculas))
print("Longitudes:", aplicar(palabras, longitudes))
