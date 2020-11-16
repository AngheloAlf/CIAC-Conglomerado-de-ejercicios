def estaPlaneta(planeta,archivo):
    arch=open(archivo)
    for linea in arch:
        if planeta in linea:
            arch.close()
            return True
    arch.close()
    return False

def agregarPlaneta(planeta,archivo,coordenadas):
    if not estaPlaneta(planeta,archivo):
        arch=open(archivo,'a')
        coord=';'.join(map(str,coordenadas))
        linea='{0}#{1}\n'
        arch.write(linea.format(planeta,coord))
        arch.close()
        return True
    return False

def obtenerCoordenadas(planeta,archivo):
    arch=open(archivo)
    for linea in arch:
        if planeta in linea:
            coord=linea.strip().split('#')[1]
            coord=map(int,coord.split(';'))
            arch.close()
            return coord

def distanciaPlanetas(planeta1,planeta2,archivo):
    coord1=obtenerCoordenadas(planeta1,archivo)
    coord2=obtenerCoordenadas(planeta2,archivo)
    suma=0
    for i in range(len(coord1)):
        suma+=(coord1[i]-coord2[i])**2
    return suma**0.5
