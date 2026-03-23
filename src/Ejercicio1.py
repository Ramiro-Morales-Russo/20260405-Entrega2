def contar_lineas(texto):
    renglones = texto.split("\n")
    return len(renglones)

def contar_palabras (texto):
    palabras = texto.split()                                             #Si usas .split(" ") no te considera los \n
    return len(palabras)

# Esto serviría para contar caracteres, no palabras, e incluiría espacios, saltos de línea, etc:
# def contar_letras (texto):
#     resultado = 0
#     resultado = [1 for palabra in texto for letra in palabra]
#     return len(resultado)

def promedio_palabras_por_linea(texto):
    promedios = []
    lista_lineas = texto.split("\n")
    for linea in lista_lineas:
        promedios.append(contar_palabras(linea))
    return (sum(promedios)/len(promedios))

def lineas_arriba_promedio(texto):
    promedio = promedio_palabras_por_linea(texto)
    lista_lineas = texto.split("\n")
    lineas = [linea for linea in lista_lineas if contar_palabras(linea)>promedio]
    return lineas


# lista_indices = []
# indice = 0
# for linea in lista_lineas:
#     if contar_palabras(linea)>promedio:
#         lista_indices.append(indice)
#     indice+=1
# return list(lista_indices)



