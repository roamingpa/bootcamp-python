import random
import sys


plantilla = """
===================================================================
     {nombre_jugador}                               OPONENTE           
===================================================================
                                         HP:  [||||||||||] {hp_actual}/{hp_base}
  STM: [<<<<<<<<<<]  {stamina_actual}/{stamina_base}                      
-------------------------------------------------------------------

     (O)   <-- Cabeza                       (O)   <-- Cabeza
    /||\   <-- Cuerpo                      /||\   <-- Cuerpo
    /|||                                   /|||
    /  \   <-- Piernas                     /  \   <-- Piernas

===================================================================
"""
# import os
# os.system('cls')

# PEDIR EL NOMBRE DEL JUGADOR
# python main.py luis
nombre_jugador = str(sys.argv[1])

# DEFINIR EL HP DEL OPONENTE
hp_base = 100
hp_actual = hp_base
# DEFINIR EL DMG (CADA ACIERTO VAN A SER 20PTS DE DMG)
dmg_base = 25
# DEFINIR LA STAMINA BASE
stamina_base = 5
stamina_actual = stamina_base

# DEFINIR LUGARES DE POSIBLES ATAQUES
lugares_del_cuerpo = {"cabeza", "cuerpo", "piernas"}

print(plantilla.format(
    nombre_jugador=nombre_jugador, 
    hp_actual=hp_actual, 
    hp_base=hp_base,
    stamina_base=stamina_base,
    stamina_actual= stamina_actual,
))

# CICLO (EN BASE A LA (STAMINA HP 0)))
while (stamina_actual > 0 and hp_actual > 0):
    # PREGUNTARLE AL USUARIO DONDE VA A ATACAR
    lugar_de_ataque = input("Escoge donde vas a atacar: ")
    if lugar_de_ataque.lower() not in lugares_del_cuerpo:
        print(f"Ingrese un valor válido: {lugares_del_cuerpo}")
        continue # continuar con un nuevo ciclo
    # PC ESCOGE DONDE VA A BLOQUEAR
    lugar_a_bloquear = random.choice(list(lugares_del_cuerpo))
    # CALCULO DEL DMG -> BLOQUEO O NO BLOQUEO -> 0 20
    if lugar_de_ataque == lugar_a_bloquear:
        dmg = 0 # oponente bloquea el ataque
    else:
        dmg = dmg_base # el ataque hace daño
    # ACTUALIZAR HP
    hp_actual -= dmg
    # RESTAR LA STAMINA
    stamina_actual -= 1
    # ACTUALIZAR LA PLANTILLA (ACTUALIZAR HP, STAMINA, Y NOMBRAR LAS DECISION)
    print(plantilla.format(
        nombre_jugador=nombre_jugador, 
        hp_actual=hp_actual, 
        hp_base=hp_base,
        stamina_base=stamina_base,
        stamina_actual= stamina_actual,
    ))
    print(f"Escogiste {lugar_de_ataque}")
    print(f"Oponente bloquea en {lugar_a_bloquear}")
    if dmg == 0:
        print("El daño es 0, no pasa el ataque")
    else:
        print(f"El daño es {dmg}, pasa el ataque!")

# mostrar los resultados
if hp_actual == 0:
    print("Has derrotado a tu oponente!!!!!!")
elif stamina_actual == 0:
    print("Te has quedado sin stamina, juega otra vez!")


### nuevo comentario