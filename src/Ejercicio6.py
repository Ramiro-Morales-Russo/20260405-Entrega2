def extraer_hashtags(posts):
    lista_palabras = []
    lista_hashtags = []
    for elemento in posts:
        palabras_elemento = (elemento.split(" "))
        for elemento in palabras_elemento:
            lista_palabras.append(elemento)
    for elemento in lista_palabras:
        if(elemento[0] == '#'):
            lista_hashtags.append(elemento)
    return lista_hashtags

def contar_unicos(palabras):
    palabras_unicas = set(palabras)
    return int(len(palabras_unicas))