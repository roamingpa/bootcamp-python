# Ejercicio 16: eliminar duplicados con set
# Enunciado: el usuario ingresa 8 números enteros. Guárdalos en una lista,
#             luego conviértela a set para quedarte solo con los únicos.
#             Muestra la lista original y los valores únicos.
# Input de ejemplo: 5, 3, 8, 3, 1, 5, 7, 1
# Output esperado:
# Lista original: [5, 3, 8, 3, 1, 5, 7, 1]
# Valores unicos: {1, 3, 5, 7, 8}

numeros = []
for i in range(8):
    n = int(input(f"Numero {i + 1}: "))
