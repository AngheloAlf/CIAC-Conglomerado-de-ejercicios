def buscar_por_raza(archivo, raza):
    arch = open(archivo)
    lista = list()
    for linea in arch:
        nombre, raza2, estado, puntaje = linea.strip().split(";")
        if raza == raza2:
            tupla = (nombre, raza, estado, puntaje)
            lista.append(tupla)
    arch.close()
    return lista

def mejor_candidato(archivo, estado):
    arch = open(archivo)
    datosMejor = list()
    puntajeMejor = 0
    for linea in arch:
        nombre, raza2, estado2, puntaje = linea.strip().split(";")
        if int(puntaje) > int(puntajeMejor):
            if estado == estado2:
                puntajeMejor = puntaje
                datosMejor = [nombre, raza2, estado, puntaje]
    arch.close()
    return datosMejor

def actualizar_puntaje(archivo, nombre, puntaje_nuevo):
    arch = open(archivo)
    lineasArchivo = list()
    plantilla = "{0};{1};{2};{3}\n"
    for linea in arch:
        nombre2, raza2, estado2, puntaje = linea.strip().split(";")
        if nombre == nombre2:
            datos = plantilla.format(nombre, raza2, estado2, str(puntaje_nuevo))
            lineasArchivo.append(datos)
        else:
            lineasArchivo.append(linea)
    arch.close()
    arch = open(archivo, "w")
    for linea in lineasArchivo:
        arch.write(linea)
    arch.close()
    return