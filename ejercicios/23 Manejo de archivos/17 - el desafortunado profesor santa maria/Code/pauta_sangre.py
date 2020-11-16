def donantes(tipo_sangre):
    compatibilidad=open('compatibilidad.txt')
    cont_linea=1
    for linea in compatibilidad:
        if cont_linea==1:
            grupos=linea.strip().split(';')
            indice=grupos.index(tipo_sangre)
        elif indice==cont_linea-2:
            info_compatibilidad=linea.strip().split(';')
        cont_linea+=1
    compatibilidad.close()
    lista_donantes=[]
    for i in range(len(grupos)):
        if info_compatibilidad[i]=='1':
            lista_donantes.append(grupos[i])
    donantes=open('donantes.txt','w')
    sangre=open('sangre.txt')
    for linea in sangre:
        datos=linea.strip().split(';')
        if datos[1]+datos[2] in lista_donantes:
            donantes.write(linea)
    sangre.close()
    donantes.close()
    
        
            
