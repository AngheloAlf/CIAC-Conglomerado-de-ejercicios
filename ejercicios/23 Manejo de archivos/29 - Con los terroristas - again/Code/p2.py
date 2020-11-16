def datosATuplas(datitos):
    return tuple(datitos.split(">"))

def seConocen(terroristas, terro1, terro2):
    lugares1, lugares2 = set(), set()
    arch = open(terroristas)
    for linea in arch:
        codigo, datos = linea.strip().split(";")
        datos = map(datosATuplas, datos.split(","))
        if int(codigo) == terro1:
            lugares1 = set(datos)
        elif int(codigo) == terro2:
            lugares2 = set(datos)
    arch.close()
    if lugares1&lugares2:
        return True
    return False

def habilidadesUnicas(terroristas):
    terros = dict()
    arch = open(terroristas)
    for linea in arch:
        codigo, _ = linea.strip().split(";")
        arch2 = open(codigo+".txt")
        codigo = int(codigo)
        terros[codigo] = set()
        for linea2 in arch2:
            terros[codigo].add(linea2.strip())
        arch2.close()
    arch.close()
    terros2 = dict(terros)
    for codigo in terros.keys():
        for codigo2 in terros2.keys():
            if codigo != codigo2:
                terros[codigo] -= terros2[codigo2]
    return terros

def terroristasPeligrosos(terroristas):
    habUnicas = habilidadesUnicas(terroristas)
    peligrosos = dict()
    for codigo in habUnicas:
        if len(habUnicas[codigo]) == 0:
            continue
        peligrosos[codigo] = True
        for codigo2 in habUnicas:
            if codigo != codigo2:
                if seConocen(terroristas, codigo, codigo2):
                    peligrosos[codigo] = False
                    break
    return peligrosos