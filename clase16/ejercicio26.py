# Ejercicio 26: IMC con validacion incompleta
# Enunciado: pide peso (kg) y altura (m), calcula IMC y clasifica.
# En este ejercicio, import sirve para usar floor de math y ajustar el valor mostrado.
# Input de ejemplo: peso = 70, altura = 1.75
# Output esperado (si se corrige): IMC: 22.86 | Clasificacion: Normal
# Formula de referencia (si se corrige): imc = peso / altura ^ 2
import math

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / altura ** 2
imc_mostrado = math.floor(imc)

if imc_mostrado < 18.5:
    clasificacion = "Bajo peso"
elif imc_mostrado < 25:
    clasificacion = "Normal"
elif imc_mostrado < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"IMC: {imc_mostrado:.2f}")
print(f"Clasificacion: {clasificacion}")
