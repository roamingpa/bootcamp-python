import sys

cantidad_de_usuarios = {
    "Chile": 20,
    "Argentina": 10,
    "Bolivia": 5,
    "Brasil":0,
}

umbral = int(sys.argv[1])

nuevo_diccionario = {}

for pais, usuarios in cantidad_de_usuarios.items():
    if usuarios > umbral:
        nuevo_diccionario[pais] = usuarios

print(nuevo_diccionario)