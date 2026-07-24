import sys

cantidad_de_usuarios = {
    "Chile": 20,
    "Argentina": 10,
    "Bolivia": 5,
    "Brasil":0,
}

umbral = int(sys.argv[1])

nuevo_diccionario = {}
contador = 0
paises = list(cantidad_de_usuarios.keys())

while contador < len(cantidad_de_usuarios):
    pais = paises[contador]
    usuarios = cantidad_de_usuarios.get(pais)
    if usuarios > umbral:
        nuevo_diccionario[pais] = usuarios
    contador += 1

print(nuevo_diccionario)