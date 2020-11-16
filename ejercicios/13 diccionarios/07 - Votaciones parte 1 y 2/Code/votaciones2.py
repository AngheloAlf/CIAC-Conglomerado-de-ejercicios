#usando conjuntos
def votos_por_cantidad(tazas):
    conj=set(tazas)
    resultados={}
    for cantidad in conj:
        resultados[cantidad]=tazas.count(cantidad)
    return resultados

#usando condiciones
def votos_por_cantidad(tazas):
    resultados={}
    for voto in tazas:
        if voto not in resultados:
            resultados[voto]=0
        resultados[voto]+=1
    return resultados

def moda(tazas):
    maximo=-float('inf')
    for cantidad,votos in votos_por_cantidad(tazas).items():
        if votos>maximo:
            moda=cantidad
            maximo=votos
    return moda

#usando listas
def promedio(tazas):
    total=0
    cont=0
    for cantidad in tazas:
        total+=cantidad
        cont+=1
    return total/cont

#usando diccionarios
def promedio2(tazas):
    total=0
    cont=0
    for cantidad,votos in votos_por_cantidad(tazas).items():
        total+=cantidad*votos
        cont+=votos
    return total/cont