def extraer_duraciones(playlist):
    duraciones = []
    for elemento in playlist:
        duraciones.append(elemento.get("duration"))
    return duraciones

def transformar_a_valor(duraciones):
    duraciones_segundos = []
    for elemento in duraciones:
        aux =[]
        aux = elemento.split(":")
        for i in range(len(aux)):
            aux[i] = int(aux[i])
        aux[0] = aux[0]*60
        duraciones_segundos.append(sum(aux))
    return duraciones_segundos

def transformar_segundos(cantidad_segundos):
    horas = 0
    minutos = 0
    segundos = 0
    resultado = []
    if cantidad_segundos>3600:
        horas = cantidad_segundos // 3600
        minutos = int(cantidad_segundos % 3600 *60)
        segundos = cantidad_segundos % 3600 *60 % 60
        resultado.append(horas)
        resultado.append(minutos)
        resultado.append(segundos)
    elif cantidad_segundos>60:
        minutos = cantidad_segundos//60
        segundos = cantidad_segundos % 60
        resultado.append(minutos)
        resultado.append(segundos)
    else:
        segundos = cantidad_segundos
        resultado.append(segundos)
    return resultado


def duracion_total(duraciones):
    segundos_totales = sum(duraciones)
    tiempo = transformar_segundos(segundos_totales)
    if len(tiempo) == 3:
        return print(f'{tiempo[0]}hs {tiempo[1]}m {tiempo[2]}s')
    elif len(tiempo)==2:
        return print(f'{tiempo[0]}m {tiempo[1]}s')
    else:
        return print(f'{tiempo[0]}s')

def max_duracion_posicion(duraciones_valor):
    indice = 0
    max_valor = 0
    max_posicion = -1
    for elemento in duraciones_valor:
        if(elemento>max_valor):
            max_valor = elemento
            max_posicion = indice
        indice+=1
    return max_posicion

def min_duracion_posicion(duraciones_valor):
    indice = 0
    min_valor = 999
    min_posicion = -1
    for elemento in duraciones_valor:
        if elemento < min_valor:
            min_valor = elemento
            min_posicion = indice
        indice += 1
    return min_posicion