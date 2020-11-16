def seConocen(terroristas, terro1, terro2):
    if terro1 not in terroristas or terro2 not in terroristas:
        return False
    datos1 = terroristas[terro1]
    datos2 = terroristas[terro2]
    for i in datos1:
        if i in datos2:
            return True
    return False
    
def terroristasFecha(terroristas, fecha):
    conj = set()
    for cod, avistados in terroristas.items():
        for lugar, fechaT in avistados:
            if fechaT == fecha:
                conj.add(cod)
    return conj

def habilidadesUnicas(habilidades):
    habUni = dict()
    for codigo, listaHabilidades in habilidades.items():
        habUni[codigo] = dict()
        for hab in listaHabilidades:
            habUni[codigo][hab] = 0
            for codigo2, lista2 in habilidades.items():
                if codigo != codigo2 and hab in lista2:
                    habUni[codigo][hab] += 1
    
    habiRetornar = dict()
    for cod, diccHabilidades in habUni.items():
        habiRetornar[cod] = set()
        for hab, cantidad in diccHabilidades.items():
            if cantidad == 0:
                habiRetornar[cod].add(hab)

    return habiRetornar

def terroristasPeligrosos(terroristas, habilidades):
    habUnicas = habilidadesUnicas(habilidades)
    peligrosos = dict()
    for cod, conjuntoHab in habUnicas.items():
        if len(conjuntoHab) != 0:
            peligrosos[cod] = True
            for otro in terroristas.keys():
                if cod != otro and seConocen(terroristas, cod, otro):
                    peligrosos[cod] = False
    return peligrosos
