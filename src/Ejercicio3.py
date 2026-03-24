def cargar_palabras(lista):
    print("Ingrese las palabras spoiler (separadas por coma): ")
    palabras = input('Ingrese una palabra: ')
    lista = palabras.split(",")
    return lista

def ocultar_spoilers(review,lista_spoilers):
    l_palabras = review.split(" ")
    resultado = [("*"*len(palabra)) if palabra in lista_spoilers else palabra for palabra in l_palabras]
    return resultado

def arreglar_review(lista_oculta):
    texto_arreglado = " ".join(lista_oculta)
    return str(texto_arreglado)
