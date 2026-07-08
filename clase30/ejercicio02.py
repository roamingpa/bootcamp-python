"""
EJERCICIO 02 — Clase Cuenta Bancaria

Enunciado:
    Crea una clase `CuentaBancaria` que simule una cuenta de banco.

    Atributo de clase:
        - banco  (str) = "Banco Python"   → compartido por todas las cuentas

    Atributos de instancia (se reciben en el constructor):
        - titular   (str)
        - saldo     (int/float)  → por defecto 0 si no se indica

    Métodos:
        - mostrar_saldo()    → imprime el titular y su saldo actual
        - depositar(monto)   → suma el monto al saldo. 
                               Si el monto es <= 0, imprime un mensaje de error.
        - girar(monto)       → resta el monto del saldo.
                               Si el monto supera el saldo, imprime un mensaje de error.
        - transferir(monto, otra_cuenta) → gira desde esta cuenta y deposita en `otra_cuenta`

    Método estático:
        - es_monto_valido(monto) → retorna True si el monto es un número mayor que 0

Input de ejemplo:
    cuenta_ana   = CuentaBancaria("Ana", 50000)
    cuenta_pedro = CuentaBancaria("Pedro")

    cuenta_ana.mostrar_saldo()
    cuenta_ana.depositar(20000)
    cuenta_ana.mostrar_saldo()
    cuenta_ana.transferir(15000, cuenta_pedro)
    cuenta_ana.mostrar_saldo()
    cuenta_pedro.mostrar_saldo()
    cuenta_ana.girar(999999)
    print(CuentaBancaria.es_monto_valido(-100))
    print(CuentaBancaria.es_monto_valido(500))

Output esperado:
    [Banco Python] Ana — Saldo: $50000
    [Banco Python] Ana — Saldo: $70000
    [Banco Python] Ana — Saldo: $55000
    [Banco Python] Pedro — Saldo: $15000
    Error: saldo insuficiente. Saldo actual: $55000
    False
    True
"""

# Escribe tu código aquí 👇


