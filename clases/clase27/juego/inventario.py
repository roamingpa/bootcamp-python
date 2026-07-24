"""
INVENTARIO:
- Añadir items al inventario (con una cantidad)
- Quitar items del inventario (con una cantidad)
- Definir la CANTIDAD DE ESPACIO MÁXIMO 10
- Cada item ocupa 1 espacio

item, cantidad


{
    "espada de madera": 0,
    "pocion de vida": 1,
    "pocion de mana": 1,
    ...
}
"""

ESPACIO_MAXIMO = 10

def calcular_espacio_disponible(inventario):
    espacio_usado = 0
    for item, cantidad in inventario.items():
        espacio_usado += cantidad 
    espacio_disponible = ESPACIO_MAXIMO - espacio_usado
    return espacio_disponible

def agregar_item(nombre, cantidad, inventario):    
    espacio_disponible = calcular_espacio_disponible(inventario)
    if espacio_disponible > 0 and espacio_disponible >= cantidad:
        inventario[nombre] = inventario.get(nombre, 0) + cantidad
    else:
        print(f"ERROR: NO SE PUDO AGREGAR ITEM {nombre}")
        print(f"-- ESPACIO DISPONIBLE: {espacio_disponible}")
        print(f"-- CANTIDAD A AGREGAR: {cantidad}")
    return inventario

def quitar_item(nombre, cantidad, inventario):    
    cantidad_item_inventario = inventario.get(nombre, 0)
    if cantidad_item_inventario >= cantidad: 
        inventario[nombre] = cantidad_item_inventario - cantidad
    else:
        print(f"ERROR: NO SE PUDO QUITAR ITEM {nombre}")
        print(f"-- CANTIDAD ITEM EN EL INVENTARIO: {cantidad_item_inventario}")
        print(f"-- CANTIDAD A QUITAR: {cantidad}")
    if inventario.get(nombre, 0) == 0:
        inventario.pop(nombre)
    return inventario

def imprimir_inventario(inventario):
    print("---INVENTARIO---")
    for item, cantidad in inventario.items():
        print(f"{item} : {cantidad}")
    print("----------------")
    
