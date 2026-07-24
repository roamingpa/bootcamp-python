
class Usuario:
    def __init__(self, email):
        self.email = email


class CuentaBancaria:
    def __init__(self, saldo:0, usuario):
        self.saldo = saldo
        self.usuario = usuario


mi_usuario = Usuario("l.@gmail.com")
mi_cuenta_bancaria = CuentaBancaria(saldo=10_000, usuario=mi_usuario)
