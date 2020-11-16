vectores=[(-1,2,0),(3,4,-7),(1,2,3),(7,0,-3),(19,7,94)]

def norma_p(vector,p):
    suma=0
    for componente in vector:
        suma+=abs(componente)**p
    return suma**(1.0/p)

def producto_punto(vector_1,vector_2):
    parcial=0
    dim1=len(vector_1)
    dim2=len(vector_2)
    if dim1!=dim2:
        return 'Error'
    else:
        i=0
        while i<dim1:
            parcial+=vector_1[i]*vector_2[i]
            i+=1
    return parcial

def suma(vector_1,vector_2):
    lista=[]
    dim1=len(vector_1)
    dim2=len(vector_2)
    if dim1!=dim2:
        return 'Error'
    else:
        i=0
        while i<dim1:
            lista.append(vector_1[i]+vector_2[i])
            i+=1
    return tuple(lista)

def norma2(vectores):
    lista=[]
    for vector in vectores:
        lista.append(round(norma_p(vector,2),3))
    return lista

def suma_total(vectores):
    cant=len(vectores)
    parcial=vectores[0]
    i=1
    while i<cant:
        parcial=suma(parcial,vectores[i])
        i+=1
    return parcial