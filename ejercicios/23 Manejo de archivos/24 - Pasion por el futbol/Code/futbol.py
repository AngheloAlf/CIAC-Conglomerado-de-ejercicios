dic={}
equipos=['progra','matfis','quimica']
for equipo in equipos:
    pg=0
    pe=0
    pp=0
    arch=open('resultados.txt')
    for linea in arch:
        datos=linea.strip().split(';')
        if equipo==datos[0]:
            if int(datos[2])>int(datos[3]):
                pg+=1
            elif int(datos[2])<int(datos[3]):
                pp+=1
            else:
                pe+=1
        elif equipo==datos[1]:
            if int(datos[2])<int(datos[3]):
                pg+=1
            elif int(datos[2])>int(datos[3]):
                pp+=1
            else:
                pe+=1
    arch.close()

    dic[equipo]=(pg+pp+pe,pg,pp,pe,pg*3+pe)

print 'EQUIPO: (PJ,PG,PP,PE,PTS)\n========================'
for equipo,tupla in dic.items():
    print equipo+':' ,tupla