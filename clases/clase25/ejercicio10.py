# Ejercicio 10 - Clase 25: crear y escribir un archivo .txt con resultados
# Enunciado: define una funcion generar_reporte(alumnos, ruta) que reciba una lista
#             de diccionarios (con claves "nombre", "nota1", "nota2", "nota3") y
#             una ruta de archivo. La funcion debe:
#               1) Calcular el promedio de las 3 notas de cada alumno.
#               2) Determinar si aprobo (promedio >= 60) o reprobo.
#               3) Escribir en el archivo una linea por alumno con el formato:
#                  NOMBRE | Promedio: XX.X | APROBADO  (o REPROBADO)
#               4) Al final escribir una linea con el total de aprobados.
#
# Input de ejemplo:
# alumnos = [
#     {"nombre": "Ana",   "nota1": 70, "nota2": 80, "nota3": 90},
#     {"nombre": "Luis",  "nota1": 40, "nota2": 50, "nota3": 55},
#     {"nombre": "Sofia", "nota1": 60, "nota2": 65, "nota3": 70},
# ]
#
# Output esperado en reporte.txt:
# Ana | Promedio: 80.0 | APROBADO
# Luis | Promedio: 48.3 | REPROBADO
# Sofia | Promedio: 65.0 | APROBADO
# ---
# Total aprobados: 2 de 3

alumnos = [
    {"nombre": "Ana",   "nota1": 70, "nota2": 80, "nota3": 90},
    {"nombre": "Luis",  "nota1": 40, "nota2": 50, "nota3": 55},
    {"nombre": "Sofia", "nota1": 60, "nota2": 65, "nota3": 70},
]


def generar_reporte(alumnos, ruta):
    aprobados = 0
    with open(ruta, "w", encoding="utf-8") as archivo:
        for alumno in alumnos:
            pass  # calcula promedio, determina estado y escribe la linea
        # escribe la linea final con el total de aprobados
        pass
    print(f"Reporte guardado en {ruta}")


generar_reporte(alumnos, "reporte.txt")
