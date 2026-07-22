import preguntas as p
from string import ascii_uppercase


def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(f"{enunciado[0]}")
    print("")

    for index, alternativa in enumerate(alternativas):
        print(f"{ascii_uppercase[index]}. {alternativa[0]}")
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4