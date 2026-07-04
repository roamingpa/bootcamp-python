idioma = "español"
print(f"SCOPE GLOBAL: El idioma es: {idioma}")

def filtrar(es_mayor=True):
    global idioma
    resultado_por_defecto = 5
    print(f"DENTRO DE FILTRAR: El idioma es: {idioma}")
    idioma = "ruso"
    print(f"DENTRO DE FILTRAR: El idioma es: {idioma}")

    print(f"El resultado es: {str(resultado_por_defecto)}")
    return resultado_por_defecto

print("Empezando el programa")
resultado = filtrar()
print(f"SCOPE GLOBAL: El idioma es: {idioma}")




...
if idioma == "español":
    ...
elif idioma == "":
    ...