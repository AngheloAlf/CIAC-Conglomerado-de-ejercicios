def costo_total(arch):
    a = open(arch)
    contador = 0
    for linea in a:
    	contador += int(linea.strip())
    a.close()
    return contador

def busqueda_por_mes(arch, mes):
    a = open(arch)
    dicc = dict()
    for linea in a:
        rut, datos = linea.strip().split("#")
        for viajes in datos.split(";"):
            mes2, pais, _ = viajes.split(",")
            if mes2 == mes:
                if rut not in dicc:
                    dicc[rut] = list()
                dicc[rut].append(pais)
    a.close()
    return dicc

def obtener_costo(arch, indice):
    a = open(arch)
    contador = 1
    for linea in a:
        if contador == indice:
            a.close()
            return int(linea.strip())
        contador += 1
    a.close()
    return 0

def realizar_sumario(arch1, arch2):
    viajes = open(arch1)
    dicc = dict()
    for linea in viajes:
        rut, datos = linea.strip().split("#")
        for viajes in datos.split(";"):
            mes, pais, indice = viajes.split(",")
            costo = obtener_costo(arch2, int(indice))
            if rut not in dicc:
                dicc[rut] = [costo, [pais]]
            else:
                dicc[rut][0] += costo
                dicc[rut][1].append(pais)
    viajes.close()
    formato = "{0},{1},{2}\n"
    sumario = open("sumario.txt", "w")
    for rut, datos in dicc.items():
        costo, paises = datos
        if costo => 10000000:
            cosa = formato.format(rut, str(costo), ";".join(paises))
            sumario.write(cosa)
    sumario.close()
    