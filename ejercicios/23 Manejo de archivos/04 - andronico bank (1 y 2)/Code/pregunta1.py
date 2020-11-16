# Pregunta 2. Certamen 3. Segundo Semestre 2015.
# Andronico Bank.

# funcion apartado a):
def buscar_clientes(archivo, clase):
    datos    = dict()
    clientes = open(archivo)
    for linea in clientes:
        info_cliente = linea.strip().split(';')
        if info_cliente[2] == clase:
            datos[info_cliente[0]] = info_cliente[1]
    clientes.close()
    return datos

# funcion apartado b):
def dar_credito(archivo, rut):
    aprobacion = False
    clientes   = open(archivo)
    for linea in clientes:
        info_cliente = linea.strip().split(';')
        if info_cliente[0] == rut:
            if info_cliente[2] == 'VIP':
                aprobacion = True
    clientes.close()
    return aprobacion

# funcion apartado c):
def contar_clientes(archivo):
    datos    = dict()
    clientes = open(archivo)
    for linea in clientes:
        info_cliente  = linea.strip().split(';')
        clase_cliente = info_cliente[2]
        if clase_cliente not in datos.keys():
            datos[clase_cliente] = 1
        else:
            datos[clase_cliente] += 1
        pass
    clientes.close()
    return datos