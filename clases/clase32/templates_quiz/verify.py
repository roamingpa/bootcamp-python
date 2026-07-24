import preguntas as p


def verificar(alternativas, eleccion):
    #devuelve el índice de elección dada
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    # eleccion = 0 , 1 , 2 , 3
    # generar lógica para determinar respuestas correctas
    ##########################################################################################
    correcto = False
    # alternativas [["alt_1", 0], ["alt_2", 1], ["alt_3", 0], ["alt_4", 0]]
    for indice, alternativa in enumerate(alternativas):
        if alternativa[1] == 1 and indice == eleccion:
            correcto = True
    
    if correcto == True:
        print("LA RESPUESTA ES CORRECTA")
    else:
        print("LA RESPUESTA ES INCORRECTA")

    
    ##########################################################################################
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






