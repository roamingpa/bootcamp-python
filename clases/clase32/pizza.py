ingredientes_vegetales = ["tomate", "aceitunas", "champiñones"]
ingredientes_proteicos = ["pollo", "vacuno", "carne vegetal"]
masas = ["tradicional", "delgada"]

class Pizza:
    precio = 10_000
    tamaño = "familiar"

    @staticmethod
    def validar_elemento(opcion, ingredientes):
        return opcion in ingredientes

    def realizar_pedido(self):
        self.ingrediente_proteico = input(f"Ingrese 1 ingrediente proteico entre las siguientes opciones: \n {' -- '.join(ingredientes_proteicos)} \n")
        
        self.ingrediente_vegetal1 = input(f"Ingrese 1 ingrediente vegetal [1/2]: \n {' -- '.join(ingredientes_vegetales)} \n")
        
        self.ingrediente_vegetal2 = input(f"Ingrese 1 ingrediente vegetal [2/2]: \n {' -- '.join(ingredientes_vegetales)} \n")
        
        self.tipo_masa = input(f"Ingrese 1 tipo de masa: \n {' -- '.join(masas)} \n")

        self.es_valida = (
            self.validar_elemento(self.ingrediente_proteico, ingredientes_proteicos) and
            self.validar_elemento(self.ingrediente_vegetal1, ingredientes_vegetales) and
            self.validar_elemento(self.ingrediente_vegetal2, ingredientes_vegetales) and
            self.validar_elemento(self.tipo_masa, masas)
        )


if __name__ == "__main__":
    pizza1 = Pizza()
    pizza1.realizar_pedido()

