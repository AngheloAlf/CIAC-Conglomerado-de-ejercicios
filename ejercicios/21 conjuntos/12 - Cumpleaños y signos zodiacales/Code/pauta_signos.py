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
        
        
        
