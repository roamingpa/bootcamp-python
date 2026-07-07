"""
COLECCIONES = ITERABLES = ARRAY

CONTENEDOR QUE VA A TENER MÚLTIPLES ITEMS ADENTRO
"""

# LISTA
"""
- Items ordenado (existe un índice para cada item)
  0    1    2
["A", "B", "C"]

- Pueden ser repetidos
["A", "A", "A"]

- Son mutables: pueden modificar los items de la lista

- Pueden ser distintos tipos de datos
["A", 1, true]
"""
lista = [ "A", "B", "C" ]

print(lista)

# MÉTODOS DE LAS LISTAS

# APPEND añade un item al final de la lista
lista.append("D")
print("APPEND: " + str(lista))

# INSERT inserta un item en un indice especifico
lista.insert(1, "b")
print("INSERT: " + str(lista))

# + agregar los items de una segunda lista al final de la primera lista
lista = lista + ["E", "F"] 
print("+: " + str(lista))

# POP remover un item en un indice especifico
# por defecto elimina el último
lista.pop(1)
print("POP: " + str(lista))

lista.pop()
print("POP: " + str(lista))

# REMOVE remover la primera ocurrencia de un item
lista.remove("A")
print("REMOVE: " + str(lista))


# SORT ordenar la lista de forma alfabetica por defecto.
lista.sort()
# a,b,c   1,2,3
print("SORT: " + str(lista))

# Usamos reverse para hacerla de forma contraria
lista.sort(reverse=True)
# c,b,a  3,2,1
print("SORT REVERSE: " + str(lista))

# COUNT contar los items

print("COUNT B: " + str(lista.count("A")))

# FUNCIONES CON ARGUMENTOS TIPO LISTA
# sorted

sorted(lista)

len(lista)

# TUPLAS
"""
Inmutable = no podemos modificar los items

(1, 2) # generalmente son 2 items
(1, 2, 3, 4, ...)

destructuring = desacoplamiento
tupla = (1, 2)
item1, item2 = tupla

# DIAS DE LA SEMANA
("LUNES", "MARTES", ...)

# COORDENADAS
(12.012, 231.00)
(12.012, 231.00, -121)
"""
tupla = (1, 2)
item1, item2 = tupla
print("Item1: " + str(item1) + " Item 2" + str(item2))

print("Multiplicar items:" + str(item1 * item2))

print("Item2: " + str(item2))


# SET
"""
ITEMS ÚNICOS
[1,2,1,1,1]
set([1,2,1,1,1])
{1,2}

Son mutable al igual que las listas (se pueden volver inmutables usando el tipo de dato FrozenSet)

No podemos modificar los elementos

Podemos utilizar la teoria de conjuntos

No son ordenados
"""

# Eliminar duplicados
lista5 = [1,2,1,1,1]
set5 = set(lista5)
print("SET para eliminar duplicados: " + str(set5))

# ocupar los métodos de conjuntos

set6 = {1,2,3,4,5,6}
print("SET union: " + str(set5.union(set6)))
print("SET union: " + str(set5  | set6))

print("SET difference: " + str(set6.difference(set5)))
print("SET difference: " + str(set6 - set5))


# DICCIONARIOS

"""
{
    key: value,
    llave: valor,
    k: v
}

No estan ordenados
Acceder por clave
Podemos acceder a traves de los value, pero NO es recomendado
Las claves son únicas
"""
diccionario = {
    "A": 1,
    "a": 0,
    "B": 2,
    "C": 4,
}
# acceder a un valor de un diccionario
print("Acceder a un valor []: " + str(diccionario["C"]))

# .get acceder a un valor de un diccionario
print("Acceder a un valor .get: " + str(diccionario.get("a", "NO EXISTE")))

print("Acceder a un valor .get con valor por: " + str(diccionario.get("XXXX", "NO EXISTE")))




# STRINGS...