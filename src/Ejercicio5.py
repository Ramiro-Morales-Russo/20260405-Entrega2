def calcular_envio(paquete,zona):
    costo_total = 0
    match paquete:
        case paquete if (0 < paquete < 1 and zona == "local"):
            costo_total = 500
        case paquete if(1<paquete<5 and zona == 'local'):
            costo_total = 1000
        case paquete if(5<paquete and zona == 'local'):
            costo_total = 2000
        case paquete if (0 < paquete < 1 and zona == "regional"):
            costo_total = 1000
        case paquete if (1 < paquete < 5 and zona == "regional"):
            costo_total = 2500
        case paquete if (5 < paquete and zona == "regional"):
            costo_total = 5000
        case paquete if (0 < paquete < 1 and zona == "nacional"):
            costo_total = 2000
        case paquete if (1 < paquete < 5 and zona == "nacional"):
            costo_total = 4500
        case paquete if (5 < paquete and zona == "nacional"):
            costo_total = 8000
        case _:
            costo_total = -1
    return costo_total

