def deudaPorRut(deudas, rut):
    montoFinal = 0
    for fecha, monto in deudas[rut]:
        montoFinal += monto
    return montoFinal

def deudaTotalRut(deudas, abonos, rut):
    montoFinal = deuda_por_rut(deudas, rut)
    for fecha, monto in abonos[rut]:
        montoFinal -= monto
    return montoFinal

def dinero(deudas, abonos):
    montoFinal = 0
    for rut in deudas.keys():
        montoFinal += deuda_total_rut(deudas, abonos, rut)
    return montoFinal

def agregarDeuda(deudas, rut, fecha, monto):
    datos = [fecha, monto]
    if rut in deudas:
        deudas[rut].append(datos)
    else:
        deudas[rut] = [datos]
    return deudas

def agregarAbono(abonos, rut, fecha, monto):
    return agregar_deuda(abonos, rut, fecha, monto)
