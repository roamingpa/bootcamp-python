# Ejercicio 30: analisis de texto completo
# Enunciado: el usuario ingresa una frase. El programa debe:
#             1) Separar la frase en palabras y guardarlas en una lista.
#             2) Usar un set para mostrar las palabras unicas.
#             3) Usar un diccionario para contar cuantas veces aparece cada palabra.
#             4) Mostrar la palabra mas repetida y cuantas veces aparece.
#             5) Mostrar cuantas palabras unicas hay vs el total de palabras.
# Input de ejemplo: "el gato come el pescado y el perro come el hueso"
# Output esperado:
# Total de palabras: 11
# Palabras unicas: {'gato', 'come', 'pescado', 'y', 'perro', 'hueso', 'el'}
# Cantidad de palabras unicas: 7
# Frecuencias: {'el': 4, 'gato': 1, 'come': 2, 'pescado': 1, 'y': 1, 'perro': 1, 'hueso': 1}
# Palabra mas repetida: "el" (4 veces)

frase = input("Ingresa una frase: ")
