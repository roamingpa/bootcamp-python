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
    # 0, 1, 2, 3
    nombre = input(f"Producto {i+1}: ")
    precio = int(input(f"Precio de {nombre}: "))
    # añadir los productos al diccionario
    catalogo[nombre] = precio
   
# imprimir el diccionario
print(catalogo)
""" for loop
# imprimir el producto mas caro
# imprimir el producto mas barato
producto_mas_caro = ""
precio_mas_caro = 0
producto_mas_barato = ""
precio_mas_barato = 999999999999999
for producto, valor in catalogo.items():
    if valor > precio_mas_caro:
        producto_mas_caro = producto
        precio_mas_caro = valor
    if valor < precio_mas_barato:
        producto_mas_barato = producto
        precio_mas_barato = valor

print(f"Mas caro: {producto_mas_caro} (${precio_mas_caro})")
print(f"Mas barato: {producto_mas_barato} (${precio_mas_barato})")
"""

# podemos poner todos los precios en una lista y usar sort
# print(sorted(catalogo.values()))
# key -> diccionario["manzana"]


# convertir el catalogo a una lista y usar sort
lista_catalogo = list(catalogo.items())
lista_catalogo = sorted(lista_catalogo, key=lambda item: item[1])
# ("manzana", 450)
print(lista_catalogo)
print(f"Mas barato: {lista_catalogo[0][0]} (${lista_catalogo[0][1]})")
print(f"Mas caro: {lista_catalogo[-1][0]} (${lista_catalogo[-1][1]})")


#######################################

print("forma #3")
producto_mas_caro = max(catalogo, key=catalogo.get) 
precio_mas_alto = catalogo[producto_mas_caro]
print(f"Mas caro: {producto_mas_caro}: ${precio_mas_alto}")

producto_mas_barato = min(catalogo, key=catalogo.get) 
precio_mas_barato = catalogo[producto_mas_barato]
print(f"Mas barato: {producto_mas_barato}: ${precio_mas_barato}")
