# 1. Solicitar el nombre del estudiante
nombre_estudiante = input("Nombre del estudiante: ")
# 2. Solicitar el nombre de la asignatura
nombre_asignatura = input("Nombre de la asignatura: ")
# 3. Solicitar nota 1
nota1 = float(input("Nota 1: "))
# 4. Solicitar nota 2
nota2 = float(input("Nota 2: "))
# 5. Solicitar nota 3
nota3 = float(input("Nota 3: "))
# 6. Calcular el promedio
promedio = (nota1 + nota2 + nota3)/3
# 7. Mostrarlo al usuario
print(f"Tu promedio es: {promedio}")