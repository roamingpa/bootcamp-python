# ============================================================
#  EJERCICIO RESUMEN - Sellos de Advertencia Nutricional
#  Ley 20.606 - Chile
# ============================================================
#
# CONTEXTO:
#   Eres desarrollador en Nestle Chile. 
#  El area legal necesita
#   un programa que lea el catalogo de productos (productos.txt)
#   y determine que sellos de advertencia debe llevar cada uno
#   segun la Ley 20.606.
#
# FORMATO DEL ARCHIVO (CSV): Comma separated values (valores separados por coma)
#   - Las lineas que comienzan con # son comentarios: ignorarlas
#   - La primera linea no comentario es el encabezado (header)
#   - Las siguientes lineas son productos separados por coma
#   - Columnas: nombre, tipo, calorias, azucares, sodio, grasas_sat
#
# SELLOS POSIBLES:
#   - ALTO EN CALORIAS
#   - ALTO EN AZUCARES
#   - ALTO EN SODIO
#   - ALTO EN GRASAS SATURADAS
#
# UMBRALES (valores iguales o mayores activan el sello):
#
#              | SOLIDOS (c/100g) | LIQUIDOS (c/100ml)
#   -----------+------------------+-------------------
#   Calorias   |   >= 350 kcal    |   >= 70 kcal
#   Azucares   |   >= 22.5 g      |   >= 6 g
#   Sodio      |   >= 800 mg      |   >= 100 mg
#   Grasas sat |   >= 6 g         |   >= 3 g
#
# INSTRUCCIONES:
#   1. Leer el archivo productos.txt ignorando las lineas de comentario
#   2. Parsear cada fila usando el encabezado como referencia
#   3. Validar cada producto antes de procesarlo. Debe reportar el
#      error y continuar con el siguiente producto si encuentra:
#        a) Campo numerico vacio o ausente
#        b) Valor no convertible a numero (ej: "N/A")
#        c) Tipo invalido (solo se acepta "solido" o "liquido")
#        d) Valor numerico negativo
#   4. Para cada producto valido, determinar sus sellos
#   5. Mostrar el reporte final
#
# OUTPUT ESPERADO (ejemplo parcial):
#
#   === REPORTE DE SELLOS NESTLE CHILE ===
#
#   [ERROR] Nestle Crunch: campo 'calorias' esta vacio
#   [ERROR] Nescafe Decaf Soluble: campo 'sodio' no es un numero valido
#   [ERROR] Maggi Crema de Champiñones: tipo 'semiliquido' no es valido
#   [ERROR] Nestle Aquarel Con Limon: campo 'calorias' no puede ser negativo
#
#   Producto : Kit Kat Original
#   Tipo     : solido
#   Sellos   : ALTO EN CALORIAS | ALTO EN AZUCARES | ALTO EN GRASAS SATURADAS
#
#   Producto : Nescafe Gold Puro
#   Tipo     : solido
#   Sellos   : SIN SELLOS
#
#   Producto : Milo Bebida Lista
#   Tipo     : liquido
#   Sellos   : ALTO EN CALORIAS | ALTO EN AZUCARES | ALTO EN SODIO
#
#   ... (un bloque por cada producto valido)
#
# DESAFIO EXTRA:
#   - Mostrar al final cuantos productos validos tienen cada sello
#   - Ordenar los productos de mayor a menor cantidad de sellos
# ============================================================

# Tu codigo aqui:

# Leer el archivo productos.txt 
# contexto
encabezado = None
productos = None

with open("productos.txt", "r", encoding="utf-8") as archivo:
    # leer todo el texto del archivo
    # texto = archivo.read()

    # leyendo linea por linea el archivo
    for indice, linea in enumerate(archivo):
        if not linea.startswith("#"):
            encabezado = linea.strip().split(",")
            print(encabezado)
            break  
    
    productos = [
        linea.strip().split(",") for linea in archivo
    ]
    print(productos)

"""
#   [ERROR] Nestle Crunch: campo 'calorias' esta vacio
#   [ERROR] Nescafe Decaf Soluble: campo 'sodio' no es un numero valido
#   [ERROR] Maggi Crema de Champiñones: tipo 'semiliquido' no es valido
#   [ERROR] Nestle Aquarel Con Limon: campo 'calorias' no puede ser negativo
"""
indices_con_errores = []
for indice_producto, producto in enumerate(productos):
    for indice, atributo in enumerate(producto):
        # validamos que los campos no esten vacios
        if atributo == "":
            print(f"[ERROR] {producto[0]}: campo '{encabezado[indice]}' esta vacio")
            indices_con_errores.append(indice_producto)
        elif indice == 1 and (atributo != "liquido" and atributo != "solido"):
            print(f"[ERROR] {producto[0]}: tipo '{atributo}' no es válido")
            indices_con_errores.append(indice_producto)
        elif indice == 2 and (float(atributo) < 0):
            print(f"[ERROR] {producto[0]}: campo '{encabezado[indice]}' no puede ser negativo")
            indices_con_errores.append(indice_producto)
        
for indice, producto in enumerate(productos):
    if indice in indices_con_errores:
        continue
    sellos = []
    tipo = producto[1]
    if tipo == "solido":
        if float(producto[2]) >= 350:
            sellos.append("ALTO EN CALORIAS")
        if float(producto[3]) >= 22.5:
            sellos.append("ALTO EN AZUCARES")
        if float(producto[4]) >= 800:
            sellos.append("ALTO EN CALORIAS")
        if float(producto[5]) >= 6:
            sellos.append("ALTO EN GRASAS SATURADAS")
    elif tipo == "liquido":
        if float(producto[2]) >= 70:
            sellos.append("ALTO EN CALORIAS")
        if float(producto[3]) >= 6:
            sellos.append("ALTO EN AZUCARES")
        if float(producto[4]) >= 100:
            sellos.append("ALTO EN CALORIAS")
        if float(producto[5]) >= 3:
            sellos.append("ALTO EN GRASAS SATURADAS")
    
    print(f"Producto : {producto[0]}")
    print(f"Tipo     : {producto[1]}")
    print(f"Sellos   : {sellos}")
    print("")



