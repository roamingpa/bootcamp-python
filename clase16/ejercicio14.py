# Ejercicio 14: convertir tiempo a segundos
# Enunciado: pide horas, minutos y segundos y devuelve el total en segundos.
# Input de ejemplo: horas = 1, minutos = 1, segundos = 1
# Output esperado (si se corrige): Total en segundos: 3661

horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
total_segundos = horas * 3600 + minutos * 60 + segundo
print(f"Total en segundos: {total_segundos}")
print(f"Mitad del total: {total_segundos / 0}")
