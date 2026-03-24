def contiene_arroba(mail):
    contiene = False
    for elemento in mail:
        if(elemento == '@'):
            contiene = True
    return contiene

def contiene_caracter_pre_arroba(mail):
    posicion_arroba = -1
    indice = 0
    for elemento in mail:
        if(elemento == '@'):
            posicion_arroba = indice
        indice+=1
    if(posicion_arroba == 0):
        return False
    else:
        return True

def contiene_punto_post_arroba(mail):
    contiene = False
    lista_texto = mail.split('@')
    if("." in lista_texto[1]):
        contiene =True
    else:
        contiene = False
    return contiene

def valida_inicio_y_fin(mail):
    validacion = False
    primer_caracter = mail[0]
    ultimo_caracter = mail[-1]
    if (primer_caracter == '@' or primer_caracter == '.' or ultimo_caracter == '@' or ultimo_caracter == '.'):
        validacion = False
    else:
        validacion = True
    return validacion

def valida_dominio(mail):
    cantidad_caracteres = 0
    indice = -1
    while indice >= -len(mail):
        if(mail[indice] == '.'):
            break
        else:
            indice -= 1
    if (indice<=-3):
        return True
    else:
        return False

def validar_correo(mail):
    resultado = False
    if contiene_arroba(mail):
        if(contiene_caracter_pre_arroba(mail) and contiene_punto_post_arroba(mail) and valida_inicio_y_fin(mail) and valida_dominio(mail)):
            resultado = True
        else:
            resultado = False
    else:
        print('No contiene arroba')
        resultado = False
    return resultado
