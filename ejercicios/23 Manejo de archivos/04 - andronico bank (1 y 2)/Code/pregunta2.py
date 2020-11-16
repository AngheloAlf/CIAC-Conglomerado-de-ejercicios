# Pregunta 3. Certamen 3. Segundo Semestre 2015.
# Andronico Bank. Continuacion.
# apartado a):
def nuevo_cliente(archivo, rut, nombre, clase):
    datos    = []
    clientes = open(archivo)
    for linea in clientes:
        datos.append(linea.strip()+'\n')
    clientes.close()
    nuevo = ';'.join([rut, nombre, clase])
    datos.append(nuevo)
    clientes  = open(archivo, 'w')
    for linea in datos:
        clientes.write(linea)
    clientes.close()
    return None
# apartado b):
def actualizar_clase(archivo, rut, clase):
    cambio   = False
    clientes = open(archivo)
    datos    = []
    for linea in clientes:
        info_cliente = linea.strip().split(';')
        if info_cliente[0] == rut:
            info_cliente[2] = clase
            temp   = ';'.join(info_cliente) + '\n'
            cambio = True
        else:
            temp = linea.strip()+'\n'
        datos.append(temp)     
    clientes.close()
    clientes  = open(archivo,'w')
    for linea in datos:
        clientes.write(linea)
    clientes.close()
    return cambio
# apartado c):
def filtrar_clientes(archivo, clase):
    archivo_nombre = 'clientes_' + clase + '.txt'
    clientes       = open(archivo)
    clientes_clase = open(archivo_nombre, 'w')
    for linea in clientes:
        info_cliente = linea.strip().split(';')
        if info_cliente[2] == clase:
            clientes_clase.write(';'.join(
                [info_cliente[0], info_cliente[1]])+'\n')
    clientes.close()
    clientes_clase.close()
    return None