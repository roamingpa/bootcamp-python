# Ejercicio 2 - Clase 24: .get() con valor por defecto
# Enunciado: tienes un diccionario de configuración. El usuario ingresa el nombre
#             de una clave. Usa .get() para mostrar su valor; si no existe,
#             muestra "Configuracion no encontrada".
# Input de ejemplo 1: clave = "idioma"   -> Output: es
# Input de ejemplo 2: clave = "tema"     -> Output: Configuracion no encontrada

config = {
    "idioma": "es",
    "resolucion": "1920x1080",
    "volumen": 75,
    "pantalla_completa": True
}

clave = input("Ingresa el nombre de la configuracion: ")

print(config.get(clave, "Configuracion no encontrada"))
