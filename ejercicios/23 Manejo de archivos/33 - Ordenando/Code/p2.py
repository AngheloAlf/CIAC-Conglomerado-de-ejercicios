def promedio_ramo(archivo, ramo):
    arch = open(archivo)
    sumaNotas = 0.0
    total = 0.0
    for linea in arch:
        linea = linea.strip().split("#")
        if linea[1] == ramo:
            notas = linea[2].split(";")
            for nota in notas:
                sumaNotas += float(nota)
                total += 1.0
    arch.close()
    return sumaNotas/total