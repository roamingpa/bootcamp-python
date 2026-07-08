import os

masas_disponibles = ["tradicional", "delgada", "bordes de queso"]

masa = None
salsa = None
ingredientes = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_pizza(ingredientes, masa, salsa):
    limpiar_pantalla()
    print("")
    print("Su pizza actual es:")
    print(f"Masa: {masa}")
    print(f"Salsa: {salsa}")
    print(f"Ingredientes: {ingredientes}")
    print("")
    input("Presione cualquier tecla para continuar: ")

def seleccionar_masa():
    limpiar_pantalla()
    print("---SELECCIÓN DE MASA--- ")
    print("Escoja entre las siguientes opciones: ")
    for opcion, masa in enumerate(masas_disponibles):
        print(f"[{opcion}] {masa} ")
    while True:
        opcion = input("Escriba el número de su opción: ")
        # es opcion valida o no
        if opcion in "".join([str(x) for x in range(len(masas_disponibles))]):
            break
        print("Opción inválida, vuelva a intentarlo")
        print("")
    return masas_disponibles[int(opcion)]

def seleccionar_opcion():
    limpiar_pantalla()
    print("Bienvenido a Pizza Jat")
    print("Escoja entre las siguientes acciones: ")
    print("[0] Escoger masa ")
    print("[1] Escoger salsa ")
    print("[2] Escoger ingredientes ")
    print("[3] Escoger ... ")
    print("[4] Ver pizza")

    opcion = input("Escriba el número de su opción: ")
    
    if opcion == "0":
        global masa
        masa = seleccionar_masa()    
    elif opcion == "4":
        imprimir_pizza(ingredientes, masa, salsa)

while True:
    seleccionar_opcion()
    