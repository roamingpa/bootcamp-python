from personaje import Personaje

print("¡Bienvenido a Gran Fantasía!")
nombre_personaje = input("Por favor indique nombre de su personaje: ")

pj1 = Personaje(nombre_personaje)
pj2 = Personaje("Orco")

print(pj1.estado)
print("")
print("¡Oh no!, ¡Ha aparecido un Orco!")
print("")

opcion = pj1.mostrar_dialogo_enfrentamiento(pj2)
while opcion != 2:
    pj1.combatir(pj2)
    print(pj1.estado)
    print(pj2.estado)
    opcion = pj1.mostrar_dialogo_enfrentamiento(pj2)


print("¡Has huido! El orco ha quedado atrás.")

