from collections import Counter
import random

def normalizar_participantes(participantes):
    participantes_normalizados = [p.lower() for p in participantes]             #Otra forma era participantes_normalizados = list(map(str.lower,participantes))
    participantes_normalizados = [p.strip() for p in participantes_normalizados]
    return participantes_normalizados

def no_hay_repetidos(participantes):
    resultado_repetidos = True
    cantidad_repeticiones = Counter(participantes).most_common()
    for persona,cantidad in cantidad_repeticiones:
        if (cantidad>1):
            resultado_repetidos = False
    return resultado_repetidos

def validar_participantes(participantes):
    resultado_validacion = False
    p_normalizados = normalizar_participantes(participantes)
    if (len(p_normalizados) >= 3) and (no_hay_repetidos(p_normalizados)):
        resultado_validacion=True
    return resultado_validacion

def asignar_amigo(participante,posibles_asignaciones):
    posicion = random.randint(0, len(posibles_asignaciones) - 1)
    asignar = posibles_asignaciones[posicion]
    if (asignar == participante):
        posicion = asignar_amigo(participante, posibles_asignaciones)
    return posicion

def asignar_amigo_invisible(participantes):
    sin_asignar = participantes.copy()
    asignaciones = []
    for participante in participantes:
        posicion_a = asignar_amigo(participante,sin_asignar)
        asignacion = sin_asignar[posicion_a]
        asignaciones.append(f'{participante} ---> {asignacion}')
        sin_asignar.pop(posicion_a)
    texto_final = "\n".join(asignaciones)
    return texto_final