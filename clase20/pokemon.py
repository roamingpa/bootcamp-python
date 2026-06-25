import sys
import random

tipo_pokemon = str(sys.argv[1]).lower()

tipos_permitidos = {"planta", "fuego", "agua"}
if (tipo_pokemon not in tipos_permitidos):
    print(f"El tipo {tipo_pokemon} NO es permitido")
    print(f"Usa alguna de estas opciones: {tipos_permitidos}")
    sys.exit()

print(f"Mi pokémon es de tipo: {tipo_pokemon} ")

tipo_pokemon_oponente = random.choice(list(tipos_permitidos))

print(f"El pokemon del oponente es de tipo: {tipo_pokemon_oponente}")

"""
if tipo_pokemon == tipo_pokemon_oponente:
    print("El ataque no es efectivo (x0)")
elif tipo_pokemon == "planta" and tipo_pokemon_oponente == "agua":
    print("El ataque es super eficaz (x2)")
elif tipo_pokemon == "planta" and tipo_pokemon_oponente == "fuego":
    print("El ataque no es muy eficaz")
elif tipo_pokemon == "agua" and tipo_pokemon_oponente == "fuego":
    print("El ataque es super eficaz (x2)")
elif tipo_pokemon == "agua" and tipo_pokemon_oponente == "planta":
    print("El ataque no es muy eficaz")
elif tipo_pokemon == "fuego" and tipo_pokemon_oponente == "planta":
    print("El ataque es super eficaz (x2)")
elif tipo_pokemon == "fuego" and tipo_pokemon_oponente == "agua":
    print("El ataque no es muy eficaz")
"""

"""
if tipo_pokemon == tipo_pokemon_oponente:
    print("El ataque no es efectivo (x0)")
elif (
    (tipo_pokemon == "planta" and tipo_pokemon_oponente == "agua")
    or (tipo_pokemon == "agua" and tipo_pokemon_oponente == "fuego")
    or (tipo_pokemon == "fuego" and tipo_pokemon_oponente == "planta")
):
    print("El ataque es super eficaz (x2)")
elif (
    (tipo_pokemon == "planta" and tipo_pokemon_oponente == "fuego")
    or (tipo_pokemon == "agua" and tipo_pokemon_oponente == "planta")
    or (tipo_pokemon == "fuego" and tipo_pokemon_oponente == "agua")
):
    print("El ataque no es muy eficaz")
"""


if tipo_pokemon == tipo_pokemon_oponente:
    print("El ataque no es efectivo (x0)")
elif (
    (tipo_pokemon == "planta" and tipo_pokemon_oponente == "agua")
    or (tipo_pokemon == "agua" and tipo_pokemon_oponente == "fuego")
    or (tipo_pokemon == "fuego" and tipo_pokemon_oponente == "planta")
):
    print("El ataque es super eficaz (x2)")
else:
    print("El ataque no es muy eficaz")