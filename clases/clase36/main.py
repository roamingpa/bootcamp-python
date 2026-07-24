# SyntaxError: error al escribir código
"""
ashdja = == -==
"""


# IndexError: indice qué le dimos está fuera del rango de indices de la colección
"""
lista = [0,1,3]
lista[100]
"""

# ValueError: el valor que le pasamos a la función no cumple con alguna condición (ej no es un numero)
"""
int("asjdahd")
"""

# TypeError: el tipo de dato no cumple con alguna condición
"""
edad = 25
mensaje = "Tengo " + edad + " años" # Error: No puedes sumar texto y número.
print(mensaje)
"""

class Error(Exception):
    pass

class EdadError(Exception):
    def __init__(self, mensaje, edad):
        self.mensaje = mensaje
        self.edad = edad

class NombreError(Exception):
    ...

while True:
    try:
        nombre = input("Ingrese nombre:")
        if nombre == "":
            raise NombreError("El nombre no puede estar vacio.")
        edad = int(input("Ingrese edad:"))
        if edad < 0:
           raise EdadError("Edad debe ser un N° positivo.", edad)
        # lista = [0,1,3]
        # lista[100]
        break
    except ValueError as e:
        print(f"Ingresaste mal un dato, intentalo nuevamente {e}")
    except IndexError:
        print("Error en la lista")
    except EdadError as e:
        print(f"Hubo un error en el campo edad: {e}")
    except NombreError as e:
        print(f"Hubo un error en el campo nombre {e}")
    else:
        print("No hubo ninguna excepcion, siga su camino")




print(f"Hola {nombre} - Su edad es: {edad}")
