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
    resultado = []
    for palabra in lista:
        resultado.append(palabra.upper())
    return resultado

def longitudes(lista):
    return [len(palabra) for palabra in lista]


def aplicar(lista, funcion):
    return funcion(lista)


palabras = ["hola", "mundo", "python"]
print("Mayusculas:", mayusculas(palabras))
print("Longitudes:", longitudes(palabras))

print("Mayusculas:", aplicar(palabras, mayusculas))
print("Longitudes:", aplicar(palabras, longitudes))
