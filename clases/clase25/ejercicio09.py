# Ejercicio 9 - Clase 25: leer informacion desde un archivo .txt
# Enunciado: el archivo alumnos.txt contiene una lista de alumnos con el formato:
#             nombre,edad,pais  (una persona por linea)
#
#             Define una funcion leer_alumnos(ruta) que:
#               1) Abra el archivo con open() y lo lea linea por linea.
#               2) Para cada linea, separe los valores con .split(",") y arme un dict
#                  con las claves "nombre", "edad" (int) y "pais".
#               3) Retorne una lista de esos diccionarios.
#
#             Luego llama a la funcion, recorre la lista e imprime cada alumno.
#
# Input: archivo alumnos.txt (ya existe en la misma carpeta)
#
# Output esperado:
# Nombre: Ana | Edad: 22 | Pais: Chile
# Nombre: Luis | Edad: 30 | Pais: Argentina
# Nombre: Sofia | Edad: 25 | Pais: Mexico
# Nombre: Pedro | Edad: 19 | Pais: Chile
# Nombre: Maria | Edad: 28 | Pais: Colombia


def leer_alumnos(ruta):
    alumnos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        pass  # recorre las lineas, arma cada dict y agrega a alumnos
    return alumnos


alumnos = leer_alumnos("alumnos.txt")

for alumno in alumnos:
    pass  # imprime cada alumno con el formato esperado
