def calcular_puntaje(notas):
    total = 0
    for nota in notas.values():
        total += nota
    return total


def determinar_ganador(datos_por_ronda):
    ganador = max(datos_por_ronda,key=lambda x:x['puntaje']) 
    return ganador

def imprimir_ganador(ganador):
    texto_ganador = (f"Ganador: {ganador['cocinero']} con {ganador['puntaje']} puntos")
    return texto_ganador


def simular_ronda(i, ronda, datos_por_ronda):
    print(f'Ronda {i} - {ronda['theme']}: ')
    for participante, notas in ronda['scores'].items():
        puntaje = calcular_puntaje(notas)
        cocinero = participante
        numero_ronda = i
        resultado_participante = {"cocinero": cocinero, "puntaje": puntaje, "ronda": numero_ronda}
        datos_por_ronda.append(resultado_participante)
    return datos_por_ronda


def actualizar_posiciones(tabla_posiciones, datos_por_ronda, numero_ronda, ganador):
    for elemento in datos_por_ronda:
        cocinero = elemento["cocinero"]
        puntaje_actual = elemento["puntaje"]
        if (cocinero not in tabla_posiciones):
            tabla_posiciones[cocinero] = {
                "puntaje": 0,
                "rondas_ganadas": 0,
                "mejor_ronda": 0,
                "promedio": 0.0,
            }
        tabla_posiciones[cocinero]["puntaje"] += puntaje_actual
        if (cocinero == ganador["cocinero"]):
            tabla_posiciones[cocinero]["rondas_ganadas"] += 1
        if puntaje_actual > tabla_posiciones[cocinero]["mejor_ronda"]:
            tabla_posiciones[cocinero]["mejor_ronda"] = puntaje_actual
        tabla_posiciones[cocinero]["promedio"] = (tabla_posiciones[cocinero]["puntaje"] / (numero_ronda+1))
    return tabla_posiciones


def imprimir_posiciones(tabla_posiciones):
    tabla_ordenada = sorted(tabla_posiciones.items(),key=lambda x:x[1]['puntaje'],reverse=True)
    print('TABLA DE POSICIONES:')
    print(f'{'Cocinero':<15}{'Puntaje':<10}{'Rondas Ganadas':<15}{'Mejor Ronda':<10}{'Promedio':<15}')
    for participante,valores in tabla_ordenada:
        puntaje = valores['puntaje']
        ganadas = valores['rondas_ganadas']
        mejor_r = valores['mejor_ronda']
        promedio = valores['promedio']
        print(f"{participante:<15} {puntaje:<10} {ganadas:<16} {mejor_r:<13} {promedio:<10}")
    print('-'*50)
