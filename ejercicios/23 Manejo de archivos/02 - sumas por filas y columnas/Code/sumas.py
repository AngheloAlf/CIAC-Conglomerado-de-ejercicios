def suma_lineas(nombre_archivo):
    lista=[]
    archivo=open(nombre_archivo)
    for linea in archivo:
        numeros=linea.strip().split()
        numeros=map(int,numeros)
        lista.append(sum(numeros))
    archivo.close()
    return lista

def suma_columnas(nombre_archivo):
    lista=[]
    #Se crea una lista con contadores
    arch=open(nombre_archivo)
    for linea in arch:
        n=len(linea.split())
        break
    arch.close()
    for i in range(n):
        lista.append(0)
    #Se procede a sumar por columnas
    arch=open(nombre_archivo)
    for linea in arch:
        datos=map(int,linea.strip().split())
        for i in range(n):
            lista[i]+=datos[i]
    arch.close()
    return lista   
        
