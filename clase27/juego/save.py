"""
{
    "atributos": {},
    "estadisticas": {},
    "inventario": {},
}
"""
import os

def leer_archivo_guardado():
    # saber si el archivo existe o no
    if not os.path.exists("mi_pj.txt"):
        return None
    with open("mi_pj.txt", "r", encoding="utf-8") as archivo:
        informacion_pj = archivo.read()
    return eval(informacion_pj)


def sobreescribir_archivo_guardado(atributos, estadisticas, inventario):
    informacion_pj = {
        "atributos": atributos,
        "estadisticas": estadisticas,
        "inventario": inventario,
    }
    with open("mi_pj.txt", "w", encoding="utf-8") as archivo:
       archivo.write(repr(informacion_pj))
