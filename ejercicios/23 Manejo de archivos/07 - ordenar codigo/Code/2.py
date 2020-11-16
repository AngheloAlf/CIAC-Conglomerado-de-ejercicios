def crear_archivo():
    brutos=open('brutos.txt','w')
    clientes=open('clientes.txt')
    for linea1 in clientes:
        datos1=linea1.strip().split(':')
        descuentos=open('descuentos.txt')
        for linea2 in descuentos:
            datos2=linea2.strip().split(':')
            if datos1[0]==datos2[0]:
                final=int((int(datos1[-1])-int(datos2[-1]))*1.19)
                line='{0}:{1}:{2}:{3}\n'
                brutos.write(line.format(datos1[0],datos1[-1],datos2[-1],final))
        descuentos.close()
    clientes.close()
    brutos.close()
