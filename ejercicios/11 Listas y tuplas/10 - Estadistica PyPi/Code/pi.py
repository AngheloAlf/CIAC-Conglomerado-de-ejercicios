pi=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]

def numerosEn(lista):
    nueva=[]
    for i in lista:
        if i not in nueva:
            nueva.append(i)
    return nueva

def cuantasVeces(numero,lista):
    contador=0
    for i in lista:
        if i==numero:
            contador+=1
    return contador
    # o si no le gustan los desafios
    # return lista.count(numero)

def moda(lista):
    max_veces=-float('inf')
    for numero in numerosEn(lista):
        cuantas=cuantasVeces(numero,lista)
        if cuantas>max_veces:
            max_veces=cuantas
            repetido=numero
    return repetido

def promedio(lista):
    suma,cont=0.0,0.0
    for numero in lista:
        suma+=numero
        cont+=1
    return suma/cont
    # o si le gusta ahorrar tiempo, lapiz y hojas
    # return float(sum(lista))/len(lista)

def corte(lista):
    mayores=[]
    menores=[]
    prom=promedio(lista)
    for numero in numerosEn(lista):
        if numero>=prom:
            mayores.append(numero)
        else:
            menores.append(numero)
    return (mayores,menores)

def varianza(lista):
    n=len(lista)
    prom=promedio(lista)
    suma=0.0
    for numero in lista:
        suma+=(numero-prom)**2
    return suma/n

def mapear(funcion,lista):
    nueva=[]
    for numero in lista:
        nueva.append(funcion(numero))
    return nueva
    # o si...
    # return map(funcion,lista)


    
    
    
