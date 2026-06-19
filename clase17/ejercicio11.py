# Ejercicio 11: ordenar una lista
# Enunciado: pide al usuario 5 números enteros, guárdalos en una lista y
#             muéstralos ordenados de menor a mayor y de mayor a menor.
# Input de ejemplo: 3, 7, 1, 9, 4
# Output esperado:
# Ordenado ascendente: [1, 3, 4, 7, 9]
# Ordenado descendente: [9, 7, 4, 3, 1]

numeros = []
for i in range(5):
    n = int(input(f"Ingresa el numero {i + 1}: "))
