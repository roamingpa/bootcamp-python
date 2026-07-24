# Ejercicio 2 - Clase 27: refactorizar codigo repetido en funciones
# Enunciado: el siguiente codigo tiene mucha repeticion. Refactorizalo creando
#             una funcion imprimir_resumen(nombre, notas) que encapsule la logica
#             repetida. El resultado final debe ser identico.
# Output esperado:
# === Ana ===
# Notas: [8, 7, 9]
# Promedio: 8.0
# === Luis ===
# Notas: [5, 6, 4]
# Promedio: 5.0
# === Maria ===
# Notas: [10, 9, 10]
# Promedio: 9.67

# CODIGO ORIGINAL (no modificar, solo usarlo como referencia):
# print("=== Ana ===")
# print("Notas:", [8, 7, 9])
# print("Promedio:", round(sum([8, 7, 9]) / len([8, 7, 9]), 2))
# print("=== Luis ===")
# print("Notas:", [5, 6, 4])
# print("Promedio:", round(sum([5, 6, 4]) / len([5, 6, 4]), 2))
# ... etc

def imprimir_resumen(nombre, notas):
    pass  # reemplaza con el codigo correcto


imprimir_resumen("Ana", [8, 7, 9])
imprimir_resumen("Luis", [5, 6, 4])
imprimir_resumen("Maria", [10, 9, 10])
