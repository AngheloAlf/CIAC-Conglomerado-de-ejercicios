def queSigno(fecha,signos):
    fecha=fecha[1:]
    for signo,(inicio,final) in signos.items():
        if inicio<=fecha<=final:
            return signo
    return 'capricornio'

def NombresMasSigno(fechas,signos):
    diccionario={}
    for nombre,fecha in fechas.items():
        diccionario[nombre]=queSigno(fecha,signos)
    return diccionario.items()

def masViejo(fechas):
    fecha_minima=(float('inf'),0,0)
    for nombre,fecha in fechas.items():
        if fecha<fecha_minima:
            fecha_minima=fecha
            older=nombre
    return older

def primerCumple(fechas):
    masTemprano=(12,32)
    for nombre,fecha in fechas.items():
        fecha=fecha[1:]
        if fecha<masTemprano:
            masTemprano=fecha
            primero=nombre
    return primero

def quienesCompartenCumple(fechas):
    diccionario={}
    for nombre,(anio,mes,dia) in fechas.items():
        if (mes,dia) not in diccionario:
            diccionario[(mes,dia)]=set()
        diccionario[(mes,dia)].add(nombre)
        #o bien la linea anterior se puede cambiar por
        diccionario[(mes,dia)]=diccionario[(mes,dia)]|{nombre}
        #---
    for llave,valor in diccionario.items():
        if len(valor)==1:
            del diccionario[llave]
    return diccionario
        
        
        
