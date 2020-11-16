def total(archivo):
    suma=0
    arch=open(archivo)
    for linea in arch:
        suma+=int(linea.strip().split(';')[-1])
    arch.close()
    return suma

def correccion(archivo,actual,inicial):
    original, temporal =open(archivo), open('temp','w')
    for linea in original:
        datos=linea.strip().split(';')
        if datos[1]=='B':
            razon=valores_IPC[actual]/valores_IPC[inicial]
            monto=float(datos[-1])*razon
            linea = ';'.join(datos[:-1])+';'+str(monto)+'\n'
        temporal.write(linea)
    original.close()
    temporal.close()
    original, temporal =open(archivo,'w'), open('temp')
    for linea in temporal:
        original.write(linea)
    original.close()
    temporal.close()