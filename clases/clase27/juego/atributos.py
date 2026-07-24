"""
ATRIBUTOS:
STR -> fuerza +6
DEX -> destreza +2
INT -> inteligencia +0
AGI -> AGILIDAD +2

Asignar atributos

{
    "STR": 0,
    "AGI": 0, 
    "INT": 0,
    "DEX": 0,
}
"""
ATRIBUTOS_SOPORTADOS = ["STR", "AGI", "INT", "DEX"]

def aumentar_atributos(nombre, cantidad, atributos):
    atributos[nombre] = atributos.get(nombre, 0) + cantidad
    return atributos

def imprimir_atributos(atributos):
    print("---ATRIBUTOS---")
    for nombre, cantidad in atributos.items():
        print(f"{nombre} : {cantidad}")
    print("----------------")

def asignar_puntos_disponibles(puntos_disponibles):
    pj_atributos = { item: 0 for item in ATRIBUTOS_SOPORTADOS}
    while puntos_disponibles > 0:
        print("")
        print(f"Puntos disponibles a asignar: {puntos_disponibles}")
        imprimir_atributos(pj_atributos)
        while True:
            nombre_atributo = input("Donde quieres asignar tus puntos: ")
            if nombre_atributo in ATRIBUTOS_SOPORTADOS:
                break
            print("ERROR, ESE ATRIBUTO NO EXISTE")
        while True:
            cantidad_a_asignar = int(input(f"Cuántos puntos quieres asignarle a {nombre_atributo}?: "))
            if cantidad_a_asignar <= puntos_disponibles:
                break
            print("ERROR, CANTIDAD A ASIGNAR ES MAYOR A LOS PUNTOS DISPONIBLES")
        pj_atributos = aumentar_atributos(nombre_atributo, cantidad_a_asignar, pj_atributos)
        puntos_disponibles -= cantidad_a_asignar
    return pj_atributos