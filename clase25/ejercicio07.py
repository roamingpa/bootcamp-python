# Ejercicio 7 - Clase 25: funciones que llaman a otras funciones
# Enunciado: crea tres funciones:
#   - calcular_descuento(precio, porcentaje): retorna el monto descontado (precio * porcentaje / 100)
#   - aplicar_iva(precio, tasa=19): retorna el precio con IVA incluido
#   - precio_final(precio, descuento, tasa=19): llama a las dos funciones anteriores
#     para calcular el precio despues de aplicar primero el descuento y luego el IVA.
#     Retorna el precio final redondeado a 2 decimales.
#
# Input de ejemplo:
#   precio_final(10000, 10)   -> descuento 10% luego IVA 19%
#   precio_final(5000, 20, 19)
#
# Output esperado:
# Precio final (10000 con 10% descuento + IVA 19%): 10710.0
# Precio final (5000 con 20% descuento + IVA 19%): 4760.0

def calcular_descuento(precio, porcentaje):
    pass  # reemplaza con el codigo correcto


def aplicar_iva(precio, tasa=19):
    pass  # reemplaza con el codigo correcto


def precio_final(precio, descuento, tasa=19):
    pass  # llama a calcular_descuento y luego a aplicar_iva


print(f"Precio final (10000 con 10% descuento + IVA 19%): {precio_final(10000, 10)}")
print(f"Precio final (5000 con 20% descuento + IVA 19%): {precio_final(5000, 20)}")
