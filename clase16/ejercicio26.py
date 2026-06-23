# Ejercicio 26: busqueda en set vs lista
# Enunciado: el usuario ingresa un nombre. Busca ese nombre en una lista
#             y también en un set. Imprime si lo encontró en cada uno.
#             Luego responde en un comentario: ¿cuál es más eficiente para
#             búsquedas y por qué?
# Input de ejemplo: nombre buscado = "Sofia"
# Output esperado:
# Encontrado en lista: True
# Encontrado en set: True
# (comentario con la explicacion)

nombres_lista = ["Ana", "Luis", "Maria", "Pedro", "Sofia", "Diego"]
nombres_set = {"Ana", "Luis", "Maria", "Pedro", "Sofia", "Diego"}

nombre = input("Ingresa el nombre a buscar: ")
