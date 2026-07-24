# Ejercicio 3 - Clase 26: **kwargs - argumentos nombrados variables
# Enunciado: define una funcion crear_perfil(**kwargs) que reciba datos de un
#             usuario como argumentos nombrados y los imprima como "clave: valor".
#             Llámala con distintas combinaciones de datos.
# Output esperado:
# -- Perfil --
# nombre: Carlos
# edad: 28
# ciudad: Santiago
# ocupacion: desarrollador

def crear_perfil(**kwargs):
    print("-- Perfil --")
    if len(kwargs) == 0:
        print("No hay información del perfil")
    for llave, valor in kwargs.items():
        print(f"{llave}: {valor}")


crear_perfil(nombre="Carlos", edad=28, ciudad="Santiago", ocupacion="desarrollador")
crear_perfil(nombre="Carlos", apellido="Cabrera")
crear_perfil(sobrenombre="Carlitos")
crear_perfil()



