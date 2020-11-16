def buscar(frase):
    lista=[]
    conj=set()
    f=frase.lower().split()
    for palabra in f:
        arch=open('palabras_en_libros.dat')
        for linea in arch:
            if palabra in linea:
                numeros=linea.strip().split(':')[1].split(',')
                conj=conj|set(numeros)
        arch.close()
    for libro in conj:
        arch=open('libros.dat')
        for linea in arch:
            if libro in linea:
                datos=tuple(linea.strip().split(':')[1:])
                lista.append(datos)
        arch.close()
    return lista
    
            
def buscar_disponibles(frase):
    lista2=[]
    lista=buscar(frase)
    for libro in lista:
        datos=':'.join(libro)
        arch=open('libros.dat')
        for linea in arch:
            if datos in linea:
                id_libro=linea.strip().split(':')[0]
                arch2=open('estado_libros.dat')
                for linea2 in arch2:
                    if id_libro in linea2:
                        estado=linea2.strip().split(':')[1]
                        if estado=='D':
                            lista2.append(libro)
                arch2.close()
        arch.close()
    return lista2

def reservar_libro(libro):
    libro=str(libro)
    arch=open('estado_libros.dat')
    arch2=open('temp.txt','w')
    for linea in arch:
        if libro in linea:
            arch2.write('{0}:P\n'.format(libro))
        else:
            arch2.write(linea)
    arch.close()
    arch2.close()
    arch=open('estado_libros.dat','w')
    arch2=open('temp.txt')
    for linea in arch2:
        arch.write(linea)
    arch.close()
    arch2.close()
    return None
