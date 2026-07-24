"""
ciclo FOR:

Nos ayuda a recorrer/iterar colecciones/iterables
strings-sets-dict-list-tupla...

[1, 2, 3, 4]
{1, 2, 3, 4}

"a123svac"
{
    "key": "value"
}


"""
iterable = ["1", "asdad", "asda"]
for item in iterable:
    print(item)

for item in "asdadsadasdas":
    print(item)

iterable = {
    "nombre": "luis",
    "apellido": "correa",
    "edad": 32,
    "es_chileno": True,
}
for llave, valor in iterable.items():
    print("Llave: " + str(llave))
    print("Valor: " + str(valor))
    print("")


# [0,1,2,3,4,5,6,7,8,9]
for contador in range(10):
    print(contador)
    print("enviar email")

print(" ")
lista = [0,1,2,3,4,5,6,7,8,9]
numero_de_items_en_la_lista = len(lista)
for contador in range(numero_de_items_en_la_lista):
    print(contador)




print("CONTINUE")
# continue: saltarnos una iteracion
for item in "asda++++aaa":
    if item == "+":
        continue
    
    print(item)

# break: terminar con el ciclo
print("BREAK")

for item in "asda++++aaa":
    if item == "+":
        break
    
    print(item)


### funciones
# return