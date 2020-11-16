def total_equipos(resultados):
    conjunto=set()
    for linea in resultados:
        datos=linea.strip().split(';')
        conjunto.add(datos[0])
        conjunto.add(datos[1])
    return conjunto

def lista_por_equipo(equipo,resultados):
    PG=0
    PP=0
    PE=0
    for linea in resultados:
        if equipo in linea:
            datos=linea.strip().split(';')
            equipo1=datos[0]
            equipo2=datos[1]
            marc1=int(datos[2])
            marc2=int(datos[3])
            if equipo==equipo1:
                if marc1>marc2:
                    PG+=1
                elif marc2>marc1:
                    PP+=1
                else:
                    PE+=1
            else:
                if marc1<marc2:
                    PG+=1
                elif marc2<marc1:
                    PP+=1
                else:
                    PE+=1
    PJ=PG+PP+PE
    puntos=PG*3+PE
    return [PJ,PG,PP,PE,puntos]

def crear_diccionario(resultados):
    dic={}
    for equipo in total_equipos(resultados):
        dic[equipo]=lista_por_equipo(equipo,resultados)
    return dic
        
        
