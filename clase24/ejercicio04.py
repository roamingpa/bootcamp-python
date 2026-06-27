# Ejercicio 4 - Clase 24: construir diccionario desde input
# Enunciado: el usuario ingresa 4 productos con su precio. Guarda cada par en un
#             diccionario. Al final muestra el producto mas caro y el mas barato
#             usando .items() para recorrerlo.
# Input de ejemplo:
#   Producto 1: manzana  / Precio: 500
#   Producto 2: pera     / Precio: 300
#   Producto 3: uva      / Precio: 800
#   Producto 4: naranja  / Precio: 450
# Output esperado:
# {'manzana': 500, 'pera': 300, 'uva': 800, 'naranja': 450}
# Mas caro: uva ($800)
# Mas barato: pera ($300)

catalogo = {}
for i in range(4):
    nombre = input(f"Producto {i + 1}: ")
    precio = int(input(f"Precio de {nombre}: "))
