
class Usuario:
    def __init__(self, email):
        self.email = email


class CuentaBancaria:
    def __init__(self, email, saldo:0 ):
        self.saldo = saldo
        self.usuario = Usuario(email=email)


mi_cuenta_bancaria = CuentaBancaria(saldo=10_000, email="l@gmail.com")