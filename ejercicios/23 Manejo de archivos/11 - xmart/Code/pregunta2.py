# Pregunta II. Xmart.

# Apartado a):
def agregar_venta(nombre_archivo, datos):
    retorno = True
    archivo = open(nombre_archivo)
    juegos   = list()
    for linea in archivo:
        juego = linea.strip().split(';')
        juegos.append(juego)
    if datos in juegos:
        retorno = False
    else:
        juegos.append(datos)
    archivo = open(nombre_archivo, 'w')    
    for i in range(len(juegos)):
        linea = ';'.join(juegos[i])
        if i == (len(juegos)-1):
            archivo.write(linea)
        else:
            archivo.write(linea+'\n')
    return retorno
        
def preventa_a_venta(archivo_venta, archivo_preventa, titulo):
    retorno  = False
    preventa = open(archivo_preventa)
    venta    = open(archivo_venta,'a')
    for linea in preventa:
        datos = linea.strip().split(';')
        if datos[0] == titulo:
            venta.write('\n'+';'.join(datos))
            retorno = True
    preventa.close()
    venta.close()
    return retorno

def buscar_juegos(archivo_venta, archivo_preventa, empresa):
    venta    = open(archivo_venta)
    preventa = open(archivo_preventa)
    juegos   = list()
    for linea in venta:
        juego = linea.strip().split(';')
        if juego[1] == empresa:
            juegos.append((juego[0], juego[1]))
    for linea in preventa:
        juego = linea.strip().split(';')
        if juego[1] == empresa:
            juegos.append((juego[0], juego[1]))
    return juegos