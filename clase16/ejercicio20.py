# Ejercicio 20: interes compuesto y ganancia real
# Enunciado: pide capital, tasa anual (%), anios e inflacion anual (%), y calcula monto final y ganancia real.
# Input de ejemplo: capital = 1000, tasa = 10, anios = 3, inflacion = 3
# Output esperado (si se corrige): Monto final: 1331.0 | Ganancia real: positiva
# Formula de referencia (si se corrige): monto_final = capital x (1 + tasa / 100) ^ anios; ganancia_real = monto_final / (1 + inflacion / 100) ^ anios - capital
capital = float(input("Capital inicial: "))
tasa = int(input("Tasa anual (%): "))
anios = int(input("Anios: "))
inflacion = int(input("Inflacion anual (%): "))

# Fallas logicas intencionales
monto_final = capital * (1 + tasa) ** anios
factor_inflacion = (1 + inflacion) ** anios
ganancia_real = monto_final - capital / factor_inflacion

print(f"Monto final: {monto_final}")
print(f"Ganancia real: {ganancia_real}")
