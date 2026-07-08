"""
EMPRESA: ACME
APP RECURSOS HUMANOS

Empleado:

atributos: caracteristicas
    - Nombre
    - Edad
    - Correo
    - Salario
    - Cargo
    - Horas trabajadas

métodos: acciones    
    - Crear correo institucional XXX
    - Trabajar XXXXXX
    - Calcular el pago XXXX 
    - Es dia laboral XXX
    - Aplicar aumento salarial XXX
    
"""

class Empleado:
    dominio_compañia = "acme.com"

    def __init__(self, nombre, edad, salario, cargo):
        ### CONSTRUCTOR
        # SE EJECUTA 1 VEZ AL CREAR LA INSTANCIA
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo
        self.horas_trabajadas = 0
        self.correo = ""
        
    def crear_correo_institucional(self):
        self.correo = f"{self.nombre}{self.edad}{self.cargo}@{self.dominio_compañia}"

    def trabajar(self, horas):
        self.horas_trabajadas += horas

    def calcular_pago(self):
        return self.horas_trabajadas * self.salario 
    
    def aumentar_salario(self, aumento):
        self.salario += aumento

    # métodos estáticos
    @staticmethod
    def es_dia_laboral(dia):
        return dia.capitalize() in ("Lunes", "Martes", "Miercoles")



