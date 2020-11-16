A=raw_input('Ingrese A: ')
B=raw_input('Ingrese B: ')
cont=0
interseccion=''
diferencia=''
while cont<len(A):
    if A[cont] in B:
        interseccion+=A[cont]
    else:
        diferencia+=A[cont]
    cont+=1
print 'interseccion:',interseccion
print 'diferencia:',diferencia