# Ejercicio 1 - Clase 26: parametros por defecto
# Enunciado: define una funcion presentar(nombre, rol="estudiante") que imprima
#             una presentacion. Si no se pasa rol, usa "estudiante" por defecto.
#             Llámala de ambas formas.
# Input de ejemplo: "Ana" / "Luis", "instructor"
# Output esperado:
# Hola, soy Ana y soy estudiante.
# Hola, soy Luis y soy instructor.

def presentar(nombre, rol="estudiante"):
    print(f"Hola, soy {nombre} y soy {rol}")

# llamar una funciona
# ejecuta esa funcion
# nombre_funcion()
# nombre_funcion(param1,param2)
presentar("Ana")
presentar("Luis", "instructor")
presentar(rol="instructor", nombre="Luis")
