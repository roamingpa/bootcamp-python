"""
Ejercicio 2 - Soporte tecnico: Por que no enciende mi computador?

Debes construir un programa interactivo que guie al usuario paso a paso
para diagnosticar por que su computador no enciende.

El programa sigue este diagrama de decision:

                          INICIO
                            |
                            v
             +------------------------------ - --+  <-----------------------+
             |  Cable de poder enchufado? (si/no)|                         |
             +------+----------------------------+                         |
                  No|                  |Si                                 |
                    v                  |                                   |
         "Conecta el cable             |                                   |
          e intenta de nuevo."         |                                   |
                    |                  |                                   |
                    +------------------+---> (si dice No, vuelve) ---------+
                                       |
                                       v
             +------------------------------------+
             |  Enciende el LED del boton? (si/no)|
             +------+-----------------------------+
                  No|                    |Si
                    v                    |
         "Puede ser la fuente            |
          de poder. Lleva a              v
          servicio tecnico."   +--------------------------+
                 FIN           | Hay imagen en pantalla?  |
                               +------+-------------------+
                                    No|              |Si
                                      v              v
                    +-----------------------+    "El computador
                    | Cable de video bien   |     esta funcionando!"
                    | conectado? (si/no)    |         FIN
                    +------+----------------+
                         Si|          |No
                            v          v
                 "Puede ser la     "Conecta el
                  GPU o pantalla.   cable de video
                  Lleva a           
                  tecnico."         "
                      FIN               FIN

Requerimientos:
- El programa debe ser completamente interactivo (usa input())
- Solo acepta respuestas "si" o "no" (en minusculas, sin tilde)
- Si el usuario ingresa una respuesta invalida, debe volver a preguntar
  esa misma pregunta hasta que responda correctamente
- Cada paso debe mostrar claramente que hacer a continuacion
- El programa termina cuando se llega a un diagnostico final

Pistas:
- Usa un while True con un break para el loop de validacion de respuesta
- Anida los if/elif dentro de cada etapa del diagnostico

----------------------------------------------------------------------
Ejemplo de sesion:

    === DIAGNOSTICO: MI COMPUTADOR NO ENCIENDE ===

    Cable de poder enchufado? (si/no): maybe
    Respuesta invalida. Ingresa "si" o "no".
    Cable de poder enchufado? (si/no): no
    -> Conecta el cable e intenta de nuevo.

    Cable de poder enchufado? (si/no): si
    Enciende el LED del boton de encendido? (si/no): no
    -> Puede ser la fuente de poder. Lleva el equipo a servicio tecnico.

----------------------------------------------------------------------
Ejemplo de sesion (flujo completo exitoso):

    === DIAGNOSTICO: MI COMPUTADOR NO ENCIENDE ===

    Cable de poder enchufado? (si/no): si
    Enciende el LED del boton de encendido? (si/no): si
    Hay imagen en la pantalla? (si/no): si
    -> El computador esta funcionando!

----------------------------------------------------------------------
"""
print("=== DIAGNOSTICO: MI COMPUTADOR NO ENCIENDE ===")

while True:
  respuesta = input("Cable de poder enchufado? (si/no): ").lower()
  if respuesta == "si":
      break
  elif respuesta == "no":
      print("Conecta el cable e intenta de nuevo")
  else:
      print('Respuesta invalida. Ingresa "si" o "no"')

while True:
  respuesta = input("Enciende el LED del boton? (si/no): ").lower()
  if respuesta == "si":
      break
  elif respuesta == "no":
      print("Puede ser la fuente de poder. Lleva a servicio técnico")
      exit()
  else:
      print('Respuesta invalida. Ingresa "si" o "no"')

while True:
  # "SI".lower() -> transformar el string a minusculas
  # "SI".upper() -> transformar el string a mayusculas
  respuesta = input("Hay imagen en pantalla? (si/no): ").lower()
  if respuesta == "si":
      print("El computador esta funcionando!")
      exit()
  elif respuesta == "no":
      break
  else:
      print('Respuesta invalida. Ingresa "si" o "no"')

while True:
  respuesta = input("Cable de video bien conectado? (si/no): ").lower()
  if respuesta == "si":
      print("Puede ser la GPU o pantalla. Lleva a técnico")
      break
  elif respuesta == "no":
      print("Conecta el cable de video")
  else:
      print('Respuesta invalida. Ingresa "si" o "no"')
