"""
EJERCICIO 03 — Cafetería Artesanal  ☕
(Mismo patrón que el desafío del té — practícalo aquí primero)

Enunciado:
    Una cafetería artesanal vende café en 3 variedades y 2 tamaños.

    Variedades:
        1 → Espresso      | preparación: 2 min  | recomendación: "Ideal para el despertar"
        2 → Cappuccino    | preparación: 4 min  | recomendación: "Perfecto para la mañana"
        3 → Cold Brew     | preparación: 8 min  | recomendación: "Refrescante en la tarde"

    Tamaños (formato):
        1 → Pequeño (200 ml) | precio: $1.500
        2 → Grande  (400 ml) | precio: $2.500

    Todos los cafés tienen una vida útil de 6 meses (180 días). → atributo de ???
    ─────────────────────────────────────────────────────────────────
    Requerimientos  (léelos todos antes de empezar)
    ─────────────────────────────────────────────────────────────────

    1. Crea la clase `Cafe` con:
       - Un ATRIBUTO DE ?? llamado `vida_util` con valor 180 (días).
       - Un `__init__` que reciba `variedad` (int) y `formato` (int).

    2. Agrega un MÉTODO ?? `info_variedad(variedad)` que reciba un entero
       (1, 2 o 3) y retorne una TUPLA con (tiempo_preparacion, recomendacion).

    3. Agrega un MÉTODO ?? `precio_por_formato(formato)` que reciba un entero
       (1 o 2) y retorne el precio correspondiente.

    4. Crea DOS instancias de `Cafe`.
       - Guarda el tipo de dato de cada instancia usando type().
       - Imprime ambos tipos.
       - Si son iguales, imprime "Ambos objetos son del mismo tipo".

    5. Escribe un pequeño programa que le pida al usuario ingresar la variedad y el
       formato, cree una instancia de `Cafe` y luego muestre por pantalla:
           - Variedad (como texto, no número)
           - Formato (como número)
           - Precio
           - Tiempo de preparación
           - Recomendación

─────────────────────────────────────────────────────────────────────────
Input de ejemplo (requerimientos 4 y 5):

    # Req 4
    c1 = Cafe(1, 1)
    c2 = Cafe(3, 2)
    tipo1 = type(c1)
    tipo2 = type(c2)
    print(tipo1)
    print(tipo2)
    # → compara e imprime el mensaje

    # Req 5 (input del usuario: variedad=2, formato=1)
    variedad ingresada: 2
    formato ingresado:  1

Output esperado:

    # Req 4
    <class '__main__.Cafe'>
    <class '__main__.Cafe'>
    Ambos objetos son del mismo tipo

    # Req 5
    Variedad: Cappuccino
    Formato: 1
    Precio: $1500
    Tiempo de preparación: 4 minutos
    Recomendación: Perfecto para la mañana
"""

# Escribe tu código aquí 👇

class Cafe:
    vida_util = 180  # atributo de clase

    def __init__(self, variedad: int, formato: int):
        self.variedad = variedad
        self.formato = formato

    @staticmethod
    def info_variedad(variedad: int) -> tuple:
        datos = {
            1: (2, "Ideal para el despertar"),
            2: (4, "Perfecto para la mañana"),
            3: (8, "Refrescante en la tarde"),
        }
        return datos[variedad]

    @staticmethod
    def precio_por_formato(formato: int) -> int:
        precios = {
            1: 1500,
            2: 2500,
        }
        return precios[formato]


# Req 4
c1 = Cafe(1, 1)
c2 = Cafe(3, 2)
tipo1 = type(c1)
tipo2 = type(c2)
print(tipo1)
print(tipo2)
if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")

# Req 5
nombres_variedad = {1: "Espresso", 2: "Cappuccino", 3: "Cold Brew"}

variedad = int(input("\nvariedad ingresada: "))
formato = int(input("formato ingresado:  "))

cafe = Cafe(variedad, formato)
tiempo, recomendacion = Cafe.info_variedad(variedad)
precio = Cafe.precio_por_formato(formato)

print(f"\nVariedad: {nombres_variedad[variedad]}")
print(f"Formato: {formato}")
print(f"Precio: ${precio}")
print(f"Tiempo de preparación: {tiempo} minutos")
print(f"Recomendación: {recomendacion}")





