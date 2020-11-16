lista_archivos = ["region1.txt","region2.txt","region3.txt"]

def juntar_archivos(lista_archivos):
	votacion_total = open("votaciontotal.txt",'w')
	for ruta in lista_archivos:
        archivo = open(ruta)
        for linea in archivo:
            linea = linea.strip()
            linea = linea.replace(':',' ').replace('/',' ').replace('#',' ')
            datos = linea.split()
            nombre, apellido, factor_votante,hora,region = datos
            factor_voto = float(hora)/float(factor_votante)
            nueva = "{0} {1}:{2}#{3}\n"
            nueva = nueva.format(apellido,nombre,region,factor_voto)
            votacion_total.write(nueva)
        archivo.close()
    votacion_total.close()
    return

def mas_popular(lista_archivos):
    #Supuesto: el mas popular es el mas votado.
    #Supuesto: Si hay dos populares se toma uno.
    #Supuesto: El orden de las regiones en el nuevo archivo no importa.
    juntar_archivos(lista_archivos)
    votacion_total = open("votaciontotal.txt")
    conteo_por_region = dict()
    #Fase de lectura
    for linea in votacion_total:
        datos = linea.strip().replace(':',' ').replace('#',' ').split()
        apellido, nombre, region, factor_voto = datos
        apellido_nombre = "{0} {1}".format(apellido, nombre)
        if region not in conteo_por_region:
            conteo_por_region[region] = dict()
        if apellido_nombre not in conteo_por_region[region]:
            conteo_por_region[region][apellido_nombre] = 0
        conteo_por_region[region][apellido_nombre] += 1
    votacion_total.close()
    #Fase de procesamiento
    votacion_popular = open("resultados.txt", "w")
    for region, candidatos in conteo_por_region.items():
        mayor = max(candidatos.values())
        apellido_nombre = ["",""]
        for candidato, cantidad in candidatos.items():
            if mayor == cantidad:
                apellido_nombre = candidato
                break
        apellido, nombre = apellido_nombre.split()
        linea = "REGION {0} {1} {2} CANTIDAD DE VOTOS {3}\n"
        region = region.replace('region','')
        nueva = linea.format(region,nombre,apellido, mayor)
        votacion_popular.write(nueva)
    votacion_popular.close()
    return

juntar_archivos(lista_archivos)
