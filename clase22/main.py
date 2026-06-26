"""
1 solo grupo
4 equipos por grupo
3 partidos por equipo

generar los enfrentamientos
pedir al usuario que nos reporte el resultado del partido
mostrar una tabla ordenada

Nombre del pais / Puntos / 
# Victorias / # Derrotas / # Empates 
Goles a favor / Goles en contra / 
Diferencia de gol /
"""

import sys
import itertools
# Definir los equipos
equipos = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]

# Generar los enfrentamientos
enfrentamientos = list(itertools.combinations(equipos, 2))
resultados = {}
for equipo in equipos:
    resultados[equipo] = {
        "Puntos": 0,
        "Victorias": 0,
        "Derrotas": 0,
        "Empates": 0,
        "Goles a favor": 0, 
        "Goles en contra": 0,
        "Diferencia de gol": 0 
    }

# Pedirle al usuario que ingrese los resultados de cada partido
for index, (equipo1, equipo2) in enumerate(enfrentamientos):
    # [("Chile", "Argentina"),("Chile", "Bolivia") ]
    print(f"Partido {index+1}: {equipo1} vs {equipo2}")
    goles_equipo1 = int(input(f"Goles de {equipo1}: "))
    goles_equipo2 = int(input(f"Goles de {equipo2}: "))
    print("")

    resultados[equipo1]["Goles a favor"] += goles_equipo1
    resultados[equipo2]["Goles a favor"] += goles_equipo2

    resultados[equipo1]["Goles en contra"] += goles_equipo2
    resultados[equipo2]["Goles en contra"] += goles_equipo1

    resultados[equipo1]["Diferencia de gol"] += (goles_equipo1 - goles_equipo2)
    resultados[equipo2]["Diferencia de gol"] += (goles_equipo2 - goles_equipo1)

    if goles_equipo1 == goles_equipo2:
        resultados[equipo1]["Empates"] += 1
        resultados[equipo2]["Empates"] += 1
        resultados[equipo1]["Puntos"] += 1
        resultados[equipo2]["Puntos"] += 1
    elif goles_equipo1 > goles_equipo2:
        resultados[equipo1]["Victorias"] += 1
        resultados[equipo2]["Derrotas"] += 1
        resultados[equipo1]["Puntos"] += 3
    elif goles_equipo2 > goles_equipo1:
        resultados[equipo2]["Victorias"] += 1
        resultados[equipo1]["Derrotas"] += 1
        resultados[equipo2]["Puntos"] += 3


# pts = victoria +3 derrota +0 empate +1

"""
{
    "Chile": {
        "Empates": 0,
        "Puntos": 2,
        "Derrotas": 3,
        ...
    },
    "Argentina": {
        "Empates": 0,
        "Puntos": 2,
        "Derrotas": 3,
        ...
    },
    "Bolivia": {
        "Empates": 0,
        "Puntos": 2,
        "Derrotas": 3,
        ...
    },
}
"""

# Ordenar los resultados
# Puntos -> DG
resultados = dict(sorted(
    resultados.items(),
    key = lambda item: (item[1]["Puntos"], item[1]["Diferencia de gol"]),
    reverse=True
))

# Mostrar la tabla de resultado
print("EQUIPO     I PTS I VICTORIAS I DERROTAS I EMPATES I GA I GC I DG")
for equipo, estadisticas in resultados.items():
    print(f'{equipo.ljust(10)} I {str(estadisticas["Puntos"]).ljust(3)} I {str(estadisticas["Victorias"]).ljust(9)} I {str(estadisticas["Derrotas"]).ljust(8)} I {str(estadisticas["Empates"]).ljust(7)} I {str(estadisticas["Goles a favor"]).ljust(2)} I {str(estadisticas["Goles en contra"]).ljust(2)} I {str(estadisticas["Diferencia de gol"]).ljust(2)}')



