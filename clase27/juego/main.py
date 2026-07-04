"""
RPG = ROLE PLAYING GAME
POKEMON 
ZELDA
DRAGON AGE
FINAL FANTASY

------------------------
INVENTARIO +
- ITEMS - CANTIDAD DE ITEMS

ESPADA BASICA X 45 
POCION X 100

CANTIDAD DE ESPACIO MÁXIMO 10


TIENDA + 

COMPRAR -> +1+2+3 X ITEMS + INVENTARIO
VENDER  -> -1-2-3 X ITEMS + INVENTARIO


ATRIBUTOS +

STR -> fuerza +6
DEX -> destreza +2
INT -> inteligencia +0
AGI -> AGILIDAD +2

OFICIAS
LISTA -> ESCOGER UN OFICIO


ESTADISTICAS
HP
MANA
"""

"""
CREACION DEL PJ:

- Tiene que ser creado al inicio del programa
- Si es que hay algun pj anteriormente creado, hay que cargarlo
- Se tiene que asignar:
   - nombre
   - escoger el oficio
   - preguntar al usuario que tipo de asignacion de atributos quiere:
        - asignar los puntos de atributos manualmente (10pts de atributo)
        - asignar atributos de forma aleatoria
   - items x defecto: 
        1 pocion 
        1 espada de madera 
        1 escudo de madera
   - oro inicial
   - asignar HP
   - asignar MANA


TIENDA
- Comprar items con una cantidad x un precio
- Vender items con una cantidadd a x precio

ESTADISTICAS:
Modificar las estadisticas
- HP (+ 1 -1)
- MANA (+ 1 -1)
- ORO (+ 1 -1)

ATRIBUTOS:
STR -> fuerza +6
DEX -> destreza +2
INT -> inteligencia +0
AGI -> AGILIDAD +2

Asignar atributos
"""
import inventario
import estadisticas
import atributos
import save

if __name__ == "__main__":
    info_pj = save.leer_archivo_guardado()
    if info_pj:
        print("TU PJ HA SIDO CARGADO CORRECTAMENTE")
        pj_inventario = info_pj["inventario"]
        pj_estadisticas = info_pj["estadisticas"]
        pj_atributos = info_pj["atributos"]
        inventario.imprimir_inventario(pj_inventario)
        estadisticas.imprimir_estadisticas(pj_estadisticas)
        atributos.imprimir_atributos(pj_atributos)
    else:
        pj_inventario = {}
        pj_inventario = inventario.agregar_item("ESPADA DE MADERA", 1, pj_inventario)
        pj_inventario = inventario.agregar_item("POCIÓN DE MANA", 2, pj_inventario)
        pj_inventario = inventario.agregar_item("POCIÓN DE HP", 2, pj_inventario)
        inventario.imprimir_inventario(pj_inventario)

        pj_estadisticas = {}
        pj_estadisticas = estadisticas.aumentar_maximo("HP", 100, pj_estadisticas)
        pj_estadisticas = estadisticas.aumentar_maximo("MANA", 50, pj_estadisticas)
        pj_estadisticas = estadisticas.aumentar_maximo("ORO", 1000, pj_estadisticas)
        estadisticas.imprimir_estadisticas(pj_estadisticas)

        pj_atributos = atributos.asignar_puntos_disponibles(10)
        atributos.imprimir_atributos(pj_atributos)
    save.sobreescribir_archivo_guardado(pj_atributos, pj_estadisticas, pj_inventario)