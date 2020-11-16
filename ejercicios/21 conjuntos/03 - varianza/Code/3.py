def varianza(conjunto):
    suma=0
    promedio=float(sum(conjunto))/len(conjunto)
    for i in conjunto:
        suma+=(i-promedio)**2
    return suma/len(conjunto)