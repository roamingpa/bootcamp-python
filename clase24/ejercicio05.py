# Ejercicio 5 - Clase 24: diccionario de frecuencias con metodos
# Enunciado: dada una lista de votos (nombres de candidatos), construye un
#             diccionario que cuente los votos de cada candidato.
#             Luego muestra el ganador y el total de votos.
# Input de ejemplo:
# votos = ["Ana","Luis","Ana","Maria","Luis","Ana","Luis","Ana","Maria","Luis"]
# Output esperado:
# Resultados: {'Ana': 4, 'Luis': 5, 'Maria': 2}
# Total de votos: 10
# Ganador/es: Luis (5 votos)

votos = ["Ana", "Luis", "Ana", "Maria", "Luis", "Ana", "Luis", "Ana", "Maria", "Luis", "Luis"]
resultados = {}

### 1
"""
for nombre in votos:
    # existe en los resultados
    if nombre in resultados:
        resultados[nombre] +=1
        # resultados[nombre] = resultados[nombre] + 1
    # no existe en los resultaddos
    else:
        resultados[nombre] = 1
"""

### 2
"""
for nombre in votos:
    resultados[nombre] = resultados.get(nombre, 0) + 1
"""
### 3
resultados = {
    nombre: votos.count(nombre) for nombre in set(votos)
}


print(f"Resultados: {resultados}")
print(f"Total de votos: {len(votos)}")
print(f"Ganador/es: {max(resultados, key=resultados.get) }")

