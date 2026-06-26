"""
Ejercicio 1 - Filtrado de inventario

Una tienda tiene su inventario registrado en un diccionario donde
la clave es el nombre del producto y el valor es el stock disponible.

inventario = {
    "manzanas": 120,
    "peras": 8,
    "naranjas": 45,
    "plátanos": 3,
    "uvas": 200,
    "sandías": 12,
    "melones": 6,
    "kiwis": 90,
    "frambuesas": 15,
    "arándanos": 4,
}

El programa debe recibir por argumento un umbral mínimo de stock y
retornar solo los productos que tengan stock MAYOR O IGUAL al umbral.

Pistas:
- Usa sys.argv para recibir el umbral
- Usa una dictionary comprehension para filtrar
- Imprime el resultado

----------------------------------------------------------------------
Ejemplo de uso:

    python ejercicio01.py 20

Salida esperada:

    {'manzanas': 120, 'naranjas': 45, 'uvas': 200, 'kiwis': 90}

----------------------------------------------------------------------
Ejemplo de uso:

    python ejercicio01.py 100

Salida esperada:

    {'manzanas': 120, 'uvas': 200}

----------------------------------------------------------------------
"""

import sys
