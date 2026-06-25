"""
Necesito ingresar mi sueldo y 
gastos del mes.
Los gastos pueden ser máximo 5, preguntar despues
de cada entrada si hay otro gasto o no. 
Si el gasto es entre 50 y 60% de mi sueldo, 
mandar un correo. 
Si el gasto es más de 60% y menor a 80%, 
hacer una llamada.
Si el gasto es 80 o sobre 80%, bloquear mis tarjetas.
Luego, necesito que mi información se muestre ordenada. 
"""

# Ingresar sueldo
import sys

sueldo = int(sys.argv[1])


# Ingresar gasto del mes n..veces hasta 5
max_gastos = 5
gastos = [] # ... 

for index in range(0, max_gastos):
    gasto = int(input("Ingresa tu gasto del mes: \n"))
    print(f"Gasto del mes #{index+1}: {gasto}")
    gastos.append(gasto)

    desea_continuar = input("Desea continuar? (si/no)\n")
    if desea_continuar.lower() == "no":
        break
    
total_gastos = sum(gastos)

# Si gasto [50 60]% del sueldo, mandar correo
if total_gastos >= (sueldo*0.5) and total_gastos <= (sueldo*0.6):
    print("Mandando un correo...")
# Si gasto [60  80]% hacer llamada
elif total_gastos >= (sueldo*0.6) and total_gastos <= (sueldo*0.8):
    print("Haciendo una llamada...")
# Si gasto [80% bloquear tarjetas 
elif total_gastos > (sueldo*0.8):
    print("Bloqueando las tarjetas...")
else:
    print("Puedes seguir gastando!")

# Imprimir información de manera ordenada

print(f"Mi sueldo es de {sueldo}")
print(f"Gastos del mes: {gastos}")
print(f"Total gastos del mes: {total_gastos}")
