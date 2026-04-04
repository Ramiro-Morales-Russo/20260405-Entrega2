import string

def cifrar_mensaje(mensaje,desplazamiento):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    cifrado = ""
    for letra in mensaje:
        if(letra in minusculas):
            posicion = minusculas.find(letra)
            nueva_posicion = (posicion+desplazamiento)%26
            cifrado += minusculas[nueva_posicion]
        elif(letra in mayusculas):
            posicion = mayusculas.find(letra)
            nueva_posicion = (posicion+desplazamiento)%26
            cifrado += mayusculas[nueva_posicion]
        else:
            cifrado+=letra
    return cifrado


def descifrar_mensaje(mensaje_cifrado,desplazamiento):
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    descifrado = ""
    for letra in mensaje_cifrado:
        if letra in minusculas:
            posicion = minusculas.find(letra)
            nueva_posicion = (posicion - desplazamiento) % 26
            descifrado += minusculas[nueva_posicion]
        elif letra in mayusculas:
            posicion = mayusculas.find(letra)
            nueva_posicion = (posicion - desplazamiento) % 26
            descifrado += mayusculas[nueva_posicion]
        else:
            descifrado += letra
    return descifrado
