# Ejercicio 17: convertir tiempo total
# Enunciado: pide horas, minutos y segundos y muestra el total en segundos y en minutos.
# Input de ejemplo: horas = 1, minutos = 2, segundos = 3
# Output esperado (si se corrige): Total segundos: 3723 | Total minutos: 62.05
horas = input("Horas: ")
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

# Fallas logicas intencionales
horas = int(horas) * 60
segundos_totales = horas + minutos + segundos
minutos_totales = segundos_totales // 60

print(f"Total segundos: {segundos_totales}")
print(f"Total minutos: {minutos_totales}")
