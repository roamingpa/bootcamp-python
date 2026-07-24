from pizza import Pizza


print("Bienvenidos a Pizza Not Jat")
print("Nuestras pizzas tienen las siguientes caracteristicas:")
print(f"Precio único de: ${Pizza.precio}")
print(f"Tamaño único: {Pizza.tamaño}")

salsa_de_tomate = "salsa de tomate"
lista_ingredientes = ["salsa de tomate", "salsa bbq"]
print(f"El elemento {salsa_de_tomate} está en la lista {lista_ingredientes}? ")
print(Pizza.validar_elemento(salsa_de_tomate, lista_ingredientes))

mi_pizza = Pizza()
mi_pizza.realizar_pedido()

print(f"Ingrediente proteico: {mi_pizza.ingrediente_proteico}")
print(f"Ingrediente vegetal 1: {mi_pizza.ingrediente_vegetal1}")
print(f"Ingrediente vegetal 2: {mi_pizza.ingrediente_vegetal2}")
print(f"Tipo de masa: {mi_pizza.tipo_masa}")
print(f"Es una pizza valida?: {mi_pizza.es_valida}")

print(Pizza.es_valida)