# Ejercicio 3 - Clase 24: .update(), .pop() y agregar claves
# Enunciado: parte del diccionario de un empleado y realiza estas operaciones:
#             1) Agrega la clave "departamento" con valor "Ventas" (asignacion directa)
#             2) Actualiza nombre y salario usando .update()
#             3) Elimina la clave "telefono" usando .pop() e imprime el valor eliminado
#             Imprime el diccionario final.
# Input de ejemplo: (ya definido abajo)
# Output esperado:
# Telefono eliminado: 555-1234
# {'nombre': 'Maria Lopez', 'edad': 30, 'salario': 850000, 'departamento': 'Ventas'}

empleado = {
    "nombre": "Juan Perez", 
    "edad": 30, 
    "salario": 750000, 
    "telefono": "555-1234"
}

# Agrega la clave "departamento" con valor "Ventas" 
empleado["departamento"] = "Ventas"

# Actualiza nombre y salario usando .update()
# Maria Lopez
"""
empleado["nombre"] = "Maria Lopez"
# 850_000
empleado["salario"] = 850_000
"""
empleado.update(nombre="Maria Lopez", salario=850_000)

# 3) Elimina la clave "telefono" usando .pop() e imprime el valor eliminado
print(empleado.pop("telefono"))

print(empleado)