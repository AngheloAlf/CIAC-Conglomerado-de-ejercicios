def estado_pasajero(nombre):
    saliDict = dict(salidas)
    for rut, (nombreP, ciudad, nacimiento, millas) in personas.items():
        if nombreP == nombre:
            for cod, conjRuts in vuelos:
                if rut in conjRuts:
                    estado = saliDict[cod][2]
                    return rut, ciudad, estado
    return None

def cambia_de_vuelo(rut, nuevo_vuelo, millas):
    if rut not in personas:
        return False
    else:
        datos = personas[rut]
        millas += datos[3]
        datos = (datos[0], datos[1], datos[2], millas)
        personas[rut] = datos
        for cod, conjRuts in vuelos:
            if rut in conjRuts:
                conjRuts.remove(rut)
            if cod == nuevo_vuelo:
                conjRuts.add(rut)
        return True

def personas_por_estado(estado):
    vuelDict = dict(vuelos)
    persDict = dict(personas)
    conj = set()

    for cod, (fec, ciudad, est) in salidas:
        if est == estado:
            for rut in vuelDict[cod]:
                datos = persDict[rut]
                nom = datos[0]
                conj.add(nom)
    return conj


def filtro_nac(fecha, estado):
    conj = set()
    for rut, (nombre, ciudad, nacimiento, millas) in personas.items():
        estado2 = estado_pasajero(nombre)[2]
        if estado == estado2 and nacimiento > fecha:
            conj.add(rut)
    return conj