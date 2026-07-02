# Ejercicio 6 - Clase 25: parametros por defecto y argumentos con nombre
# Enunciado: define una funcion crear_perfil(nombre, edad, pais="Chile", rol="estudiante")
#             que retorne un string con los datos del perfil.
#             Llamala de tres formas distintas:
#               1) Solo nombre y edad (usa los valores por defecto)
#               2) Con pais distinto al defecto
#               3) Con todos los argumentos usando argumentos con nombre (keyword args)
#
# Input de ejemplo:
#   crear_perfil("Ana", 22)
#   crear_perfil("Luis", 30, "Argentina")
#   crear_perfil(nombre="Sofia", edad=25, pais="Mexico", rol="instructora")
#
# Output esperado:
# Nombre: Ana | Edad: 22 | Pais: Chile | Rol: estudiante
# Nombre: Luis | Edad: 30 | Pais: Argentina | Rol: estudiante
# Nombre: Sofia | Edad: 25 | Pais: Mexico | Rol: instructora

def crear_perfil(nombre, edad, pais="Chile", rol="estudiante"):
    pass  # reemplaza con el codigo correcto


print(crear_perfil("Ana", 22))
print(crear_perfil("Luis", 30, "Argentina"))
print(crear_perfil(nombre="Sofia", edad=25, pais="Mexico", rol="instructora"))
