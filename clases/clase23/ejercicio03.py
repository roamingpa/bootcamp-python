"""
Ejercicio 3 - Fuerza bruta: PIN numérico

Un PIN bancario es una combinación de dígitos del 0 al 9.
En este ejercicio simularemos cuántos intentos necesita un atacante
para adivinar un PIN de N dígitos probando todas las combinaciones
posibles en orden, dígito por dígito (igual que en el ejercicio de
contraseñas con letras, pero ahora con números).

El programa pin_bruta.py debe:
1. Pedir al usuario que ingrese un PIN (solo dígitos, sin letras)
2. Intentar adivinar el PIN dígito por dígito, de izquierda a derecha
3. Para cada dígito, probar desde "0" hasta encontrar el correcto
4. Contar cada comparación como un intento
5. Mostrar cuántos intentos fueron necesarios en total

Consideraciones:
- Usa string "0123456789" (o genera los dígitos con range())
- Trata cada dígito como un string (no como número)
- El proceso es letra por letra, igual que el ejemplo del PDF
- Si el usuario ingresa algo que no son solo dígitos, muestra un error

Ejemplo paso a paso para el PIN "307":
    Dígito 1: "3"
        "0" == "3"? No  (intento 1)
        "1" == "3"? No  (intento 2)
        "2" == "3"? No  (intento 3)
        "3" == "3"? Sí  (intento 4) → siguiente dígito
    Dígito 2: "0"
        "0" == "0"? Sí  (intento 5) → siguiente dígito
    Dígito 3: "7"
        "0" == "7"? No  (intento 6)
        "1" == "7"? No  (intento 7)
        "2" == "7"? No  (intento 8)
        "3" == "7"? No  (intento 9)
        "4" == "7"? No  (intento 10)
        "5" == "7"? No  (intento 11)
        "6" == "7"? No  (intento 12)
        "7" == "7"? Sí  (intento 13) → no hay más dígitos
    Total: 13 intentos

Pistas:
- Usa un for externo para recorrer cada dígito del PIN
- Usa un for interno para probar cada dígito posible ("0" al "9")
- Usa break para pasar al siguiente dígito cuando lo encuentres
- Usa un contador que sumes en cada comparación

----------------------------------------------------------------------
Ejemplo de uso:

    python pin_bruta.py
    Ingresa el PIN: 307

    El PIN fue forzado en 13 intentos.

----------------------------------------------------------------------
Ejemplo de uso:

    python pin_bruta.py
    Ingresa el PIN: 9999

    El PIN fue forzado en 40 intentos.


----------------------------------------------------------------------
"""

import getpass

posibles_digitos = "0123456789"
pin = getpass.getpass("Ingresa el PIN: ")
while not pin.isdigit():
    print("ERROR: El pin debe solo contener numeritos")
    pin = getpass.getpass("Ingresa el PIN: ")

intentos = 0
# "1234"
for digito_objetivo in pin:
    print(f"Digito objetivo: {digito_objetivo}")
    for digito_intento in posibles_digitos:
        print(f"Digito intento: {digito_intento}")
        intentos += 1
        if digito_intento == digito_objetivo:
            print(f"Digito encontrado: {digito_objetivo} HACEN MATCH")
            break

print(f"El PIN fue forzado en {intentos} intentos")
    
