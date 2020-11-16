def total(archivo):
    suma=0
    arch=open(archivo)
    for linea in arch:
        datos=linea.strip().split(';')
        suma+=int(datos[-1])
    arch.close()
    return suma

def correccion(archivo,actual,inicial):
    original=open(archivo)
    temporal=open('temp','w')
    for linea in original:
        datos=linea.strip().split(';')
        if datos[1]=='B':
            razon=valores_IPC[actual]/valores_IPC[inicial]
            monto=round(float(datos[-1])*razon,2)
            temporal.write(';'.join(datos[:-1])+';'+str(monto)+'\n')
        else:
            temporal.write(linea)
    original.close()
    temporal.close()
    original=open(archivo,'w')
    temporal=open('temp')
    for linea in temporal:
        original.write(linea)
    original.close()
    temporal.close()
    return None

    
