anotaciones=raw_input('Anotaciones: ')
cont=0
periodo=1
suma_periodo=0
suma_total=0
periodo_terminado=False
while cont<len(anotaciones):
    letra=anotaciones[cont]
    if letra=='D':
        suma_periodo+=2
    elif letra=='L':
        suma_periodo+=1
    elif letra=='T':
        suma_periodo+=3
    elif letra==' ':
        print suma_periodo,'puntos en el periodo',periodo
        suma_total+=suma_periodo
        suma_periodo=0
        periodo+=1
    cont+=1
print suma_periodo,'puntos en el periodo',periodo
print 'Total:',suma_periodo+suma_total,'puntos'

        
        
