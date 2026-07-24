"""
ESTADISTICAS:
Modificar las estadisticas
- HP (+ 1 -1)
- MANA (+ 1 -1)
- ORO (+ 1 -1)

estadisticas = {
    "hp": (30, 110),
    "mana": (1, 50),
    "oro": (1, 9999),
}
"""

# aumentar_maximo("hp", 10, {...})
def aumentar_maximo(nombre, cantidad, estadisticas:dict[str, tuple[int, int]]):
    actual, maximo  = estadisticas.get(nombre, (0, 0))
    maximo += cantidad
    actual += cantidad
    estadisticas.update({nombre: (actual, maximo)})
    return estadisticas


def imprimir_estadisticas(estadisticas):
    print("---ESTADISTICAS---")
    for nombre, estadistica in estadisticas.items():
        print(f"{nombre} : actual {estadistica[0]} / máximo {estadistica[1]}")
    print("----------------")
    
