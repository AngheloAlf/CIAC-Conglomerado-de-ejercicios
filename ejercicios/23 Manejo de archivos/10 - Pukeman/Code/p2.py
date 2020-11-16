def promedio(datos):
    prom = 0.0
    for xi in datos:
        prom += xi
    return prom/len(datos)

def varianza(datos):
    prom = promedio(datos)
    var = 0.0
    for xi in datos:
        var += (xi-prom)**2
    return var/len(datos)

def buscarPorIde(nombres, ide):
    archNombres = open(nombres)
    nombreNuevo = ""
    for linea in archNombres:
        linea = linea.strip().split(";")
        if linea[0] == ide:
            nombreNuevo = linea[1]
    archNombres.close()
    return nombreNuevo

def mejor_Nash(pukemones, nombres):
    arch = open(pukemones)
    menorVar = float("inf")
    menorIde = ""
    for linea in arch:
        ide, stats, tipo = linea.strip().split(";")
        stats = stats.split(",")
        stats = map(int, stats)
        var = varianza(stats)
        if var < menorVar:
            menorVar = var
            menorIde = ide
    arch.close()
    return buscarPorIde(nombres, menorIde)

def mejor_Fisty(pukemones, nombres):
    arch = open(pukemones)
    sumaMayor = 0
    ideMayor = ""
    for linea in arch:
        nombre, stats, tipo = linea.strip().split(";")
        stats = stats.split(",")
        stats = map(int, stats)
        if tipo == "Grass":
            suma = stats[3]+stats[4]
            if suma > sumaMayor:
                sumaMayor = suma
                ideMayor = nombre
    arch.close()
    return buscarPorIde(nombres, ideMayor)

def filtro_Block(pukemones, nombres, saludMin):
    arch = open(pukemones)
    dicc = dict()
    for linea in arch:
        ide, stats, tipo = linea.strip().split(";")
        stats = stats.split(",")
        stats = map(int, stats)
        if tipo == "Normal" or tipo == "Electric":
            if stats[0] >= saludMin:
                dicc[ide] = (tuple(stats), tipo)
    arch.close()
    nuevoDict = dict()
    for ide, datosPuke in dicc.items():
        nuevoNombre = buscarPorIde(nombres, ide)
        nuevoDict[nuevoNombre] = datosPuke
    return nuevoDict

def quitar_pukeman(pukemones, nombres, nombrePukeman):
    archNombres = open(nombres)
    ide = ""
    for linea in archNombres:
        linea = linea.strip().split(";")
        if linea[1] == nombrePukeman:
            ide = linea[0]
    archNombres.close()
    arch = open(pukemones)
    listaArch = list()
    for linea in arch:
        ide2, stats, tipo = linea.strip().split(";")
        if ide2 != ide:
            listaArch.append(linea)
    arch.close()
    arch = open(pukemones, "w")
    for linea  in listaArch:
        arch.write(linea)
    arch.close()
    return