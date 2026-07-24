class Pizza:
    @staticmethod
    def validar_elemento_dentro_de_lista(elemento_a_validar, lista):
        return elemento_a_validar in lista
    
es_elemento_valido = Pizza.validar_elemento_dentro_de_lista(
    "salsa de tomate", 
    ["salsa de tomate", "salsa bbq"]
)
print(es_elemento_valido)
