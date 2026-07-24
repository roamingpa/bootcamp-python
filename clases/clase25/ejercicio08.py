# Ejercicio 8 - Clase 25: funciones lambda con map y filter
# Enunciado: dada la siguiente lista de productos con precio y stock:
#
#   productos = [
#       {"nombre": "Camisa", "precio": 15000, "stock": 0},
#       {"nombre": "Pantalon", "precio": 25000, "stock": 3},
#       {"nombre": "Zapatos", "precio": 40000, "stock": 0},
#       {"nombre": "Gorra", "precio": 8000, "stock": 10},
#       {"nombre": "Chaqueta", "precio": 60000, "stock": 2},
#   ]
#
#   1) Usa filter() con una lambda para obtener solo los productos CON stock (stock > 0).
#   2) Usa map() con una lambda para aplicar un 10% de descuento al precio de esos productos.
#      El resultado debe ser una lista de dicts con "nombre" y "precio_con_descuento".
#   3) Imprime cada producto con descuento.
#
# Output esperado:
# Pantalon -> $22500.0
# Gorra -> $7200.0
# Chaqueta -> $54000.0

productos = [
    {"nombre": "Camisa", "precio": 15000, "stock": 0},
    {"nombre": "Pantalon", "precio": 25000, "stock": 3},
    {"nombre": "Zapatos", "precio": 40000, "stock": 0},
    {"nombre": "Gorra", "precio": 8000, "stock": 10},
    {"nombre": "Chaqueta", "precio": 60000, "stock": 2},
]

# 1) filtra los productos con stock
con_stock = list(filter(None, productos))  # reemplaza None con la lambda correcta

# 2) aplica descuento del 10%
con_descuento = list(map(None, con_stock))  # reemplaza None con la lambda correcta

# 3) imprime los resultados
for p in con_descuento:
    pass  # reemplaza con el codigo correcto
