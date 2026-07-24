class CuentaDelBanco:
    def __init__(self, email, saldo=0):
        self.__saldo = saldo
        self.__email = email
        # l.correa.bruna@gmail.com
        # l.****@****l.com
    
    #### getter -> obtener informacion -> leer 
    @property
    def saldo(self):
        # formateo
        # filtro...
        return self.__saldo
    
    #### setter -> guardar informacion
    @saldo.setter
    def saldo(self, abono: 0):
        # validacion
        if abono > 100:
            self.__saldo += abono
        ...

    @property
    def email(self):
        # l.correa.bruna@gmail.com
        # *****rea.bruna@gmail.com
        email_anon = "*****" + self.__email[5:10] + "*****"
        return email_anon

mi_cuenta = CuentaDelBanco(saldo=1_000, email="l.correa.bruna@gmail.com")

mi_cuenta.saldo = 1_000_000
print(mi_cuenta.email)
