def leer_amigos(archivo_amigos):
    lista=[]
    archivo=open(archivo_amigos)
    for linea in archivo:
        datos=linea.strip().split(';')
        fecha=datos[-1].replace('de ','').replace('del anio ','').split()
        fecha_2='-'.join([fecha[0],fecha[1][:3],fecha[-1]])
        amigo='/'.join(datos[:3])
        lista.append( (amigo,fecha_2) )
    archivo.close()
    return lista

def cumpleaneros(archivo_amigos, archivo_saludos, fecha):
    anio=int(fecha.split()[-1])
    fecha=fecha.split(' de ')
    fecha_2=fecha[0]+'_'+fecha[1][:3]
    archivo=open('saludos-'+fecha_2+'.txt','w')
    fecha_2=fecha_2.replace('_','-')
    amigos=leer_amigos(archivo_amigos)
    for amigo in amigos:
        if fecha_2 in amigo[1]:
            arch=open(archivo_saludos)
            nombre=amigo[0].split('/')[0]
            anio_nac=int(amigo[1].split('-')[-1])
            nivel_amistad=amigo[0].split('/')[-1]
            for linea in arch:
                if nivel_amistad==linea.split(';')[0]:
                    archivo.write(linea.split(';')[1].format(nombre,anio-anio_nac))
                    archivo.write('\n')
            arch.close()
    archivo.close()
    return None
