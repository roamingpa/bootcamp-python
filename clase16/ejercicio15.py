# Ejercicio 15: interes compuesto
# Enunciado: pide capital, tasa anual y anios para calcular monto final e interes.
# Input de ejemplo: capital = 1000, tasa = 10, anios = 2
# Output esperado (si se corrige): Monto final: 1210.0 | Interes ganado: 210.0
# Formula de referencia (si se corrige): monto = capital * (1 + tasa / 100) ** anios; interes = monto - capital
capital = float(input("Capital inicial: "))
tasa = float(input("Tasa anual (%): "))
anios = int(input("Anios: "))
monto = capital * (1 + tasa / 100) ^ anios
interes = montoo - capital
print(f"Monto final: {monto}")
print(f"Interes ganado: {interes}")
