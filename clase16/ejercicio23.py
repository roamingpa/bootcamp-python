# Ejercicio 23: fecha actual formateada
# Enunciado: muestra la fecha actual en formato DD/MM/AAAA.
# En este ejercicio, import sirve para acceder a utilidades de fecha de datetime.
# Input de ejemplo: sin input
# Output esperado (si se corrige): Fecha actual: 17/06/2026
import datetime

hoy = datetime.date.today()
fecha_texto = hoy.strftime("%m/%d/%Y")

print(f"Fecha actual: {fecha_texto}")
