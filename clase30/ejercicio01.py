"""
EJERCICIO 01 — Clase Producto

Enunciado:
    Crea una clase llamada `Producto` que represente un artículo de una tienda.

    Atributos (se reciben en el constructor):
        - nombre     (str)
        - precio     (int/float)
        - stock      (int)

    Métodos:
        - mostrar_info()     → imprime el nombre, precio y stock del producto
        - vender(cantidad)   → descuenta `cantidad` del stock.
                               Si no hay suficiente stock, imprime un mensaje de error.
        - reabastecer(cantidad) → suma `cantidad` al stock
        - aplicar_descuento(porcentaje) → reduce el precio según el porcentaje dado
                               Ej: aplicar_descuento(10) baja el precio un 10%

Input de ejemplo:
    p = Producto("Teclado", 25000, 10)
    p.mostrar_info()
    p.vender(3)
    p.mostrar_info()
    p.aplicar_descuento(10)
    p.mostrar_info()
    p.vender(20)

Output esperado:
    Producto: Teclado | Precio: $25000 | Stock: 10
    Producto: Teclado | Precio: $25000 | Stock: 7
    Producto: Teclado | Precio: $22500.0 | Stock: 7
    Error: no hay suficiente stock. Stock actual: 7
"""

# Escribe tu código aquí 👇


