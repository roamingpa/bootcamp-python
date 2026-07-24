# Ejercicio 27: contrasena aleatoria reproducible
# Enunciado: genera una contrasena de 8 caracteres usando letras y digitos.
# En este ejercicio, import sirve para combinar herramientas: random para elegir y string para caracteres.
# Input de ejemplo: sin input
# Output esperado (si se corrige): Contrasena: 8 caracteres variados en cada ejecucion
import random
import string

random.seed(123)
alfabeto = string.ascii_letters + string.digits
contrasena = ""

for i in range(8):
    contrasena = random.choice(alfabeto)

print(f"Contrasena: {contrasena}")
