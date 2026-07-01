# Ejercicio 1 - Clase 24: Recorrer un diccionario con .keys(), .values() e .items()
# Enunciado: dado el diccionario de precios, imprime por separado:
#             a) Solo los nombres de productos (.keys())
#             b) Solo los precios (.values())
#             c) Cada producto con su precio (.items())
# Input de ejemplo: (ya definido abajo)
# Output esperado:
# -- Productos --
# Notebook
# Teclado
# Mouse
# -- Precios --
# 700000
# 25000
# 12000
# -- Detalle --
# Notebook: $700000
# Teclado: $25000
# Mouse: $12000

precios = {"Notebook": 700000, "Teclado": 25000, "Mouse": 12000}

print("-- Productos --")
for producto in precios.keys():
    print(producto)

print("-- Precios --")
for precio in precios.values():
    print(precio)

print("-- Detalle --")
for producto, precio in precios.items():
    print(f"{producto}: ${precio}")
