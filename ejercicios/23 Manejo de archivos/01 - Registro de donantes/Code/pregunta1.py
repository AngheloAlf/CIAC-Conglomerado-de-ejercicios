# Ejercicio I.
# Donantes.

donantes = [(15274, 'Fulana de Tal'     , 200),
            (15891, 'Jean Dupont'       , 150),
            (16443, 'Erika Mustermann'  , 400),
            (16504, 'Perico los Palotes',  80),
            (17004, 'Jan Kowalski'      , 200)] 

# 1.- Crear archivo con datos de tabla ejemplo:
def crear_archivo(donantes):
    archivo = open('donantes.txt', 'w')
    for persona in donantes:
		temp = str(persona[0]) + ':' + \
		       persona[1]      + ':' + \
		       str(persona[2]) + '\n'
		archivo.write(temp)
    archivo.close()
	
# 2.- Mostrar datos del archivo:
def mostrar_datos(nombre_archivo):
	largo = 20
	print '=============================='
	print '= Contenido archivo donantes ='
	print '==============================\n'
	print '|rut   |nombre              |donacion'
	archivo = open(nombre_archivo)
	for linea in archivo:
		datos = linea.strip().split(':')
		fit   = largo - len(datos[1]) 
		temp  = '|' + datos[0] + ' '     + \
		        '|' + datos[1] + ' '*fit + \
		        '|' + datos[2]
		print temp
	archivo.close()

# 3.- Obtener monto donado segun rut:
def monto_donado(rut, nombre_archivo):
	largo = 20
	archivo = open(nombre_archivo)
	for linea in archivo:
		datos = linea.strip().split(':')
		if rut == int(datos[0]):
			print '============'
			print '= Donacion ='
			print '============\n'
			print '|persona             |Donacion'
			fit = largo - len(datos[1])
			print '|' + datos[1] + ' '*fit + \
			      '|' + datos[2]

# 4.- Eliminar donante segun rut:
def eliminar_donante(rut, nombre_archivo):
	archivo1 = open(nombre_archivo)
	archivo2 = None
	datos    = list()
	largo    = 20
	nombre   = None
	for linea in archivo1:
		datos_rut = linea.strip().split(':')
		rut_buscado = int(datos_rut[0])
		if rut_buscado != rut:
			datos.append(linea)
		else:
			nombre = datos_rut[1]
	archivo1.close()
	archivo2 = open(nombre_archivo, 'w')
	for linea in datos:
		archivo2.write(linea)
	archivo2.close()
	print '========================'
	print '= Eliminacion donantes ='
	print '========================\n'
	print '|rut   |nombre'
	fit = largo - len(nombre) 
	print '|' + str(rut) + ' |' + nombre + ' '*fit
	
# 5.- Agregar donante ordenado segun rut:
def agregar_donante(rut, nombre, donacion, nombre_archivo):
	archivo = open(nombre_archivo)
	datos   = list()
	datos2  = list()
	nuevo   = (str(rut), nombre, str(donacion))
	for linea in archivo:
		temp = linea.strip().split(':')
		datos.append((temp[0], temp[1], temp[2]))
	archivo.close()
	for d in datos:
		if nuevo not in datos2 and int(nuevo[0]) < int(d[0]):
			datos2.append(nuevo)
			datos2.append(d)
		else:
			datos2.append(d)
	if nuevo not in datos2:
	    datos2.append(nuevo)
	archivo2 = open(nombre_archivo, 'w')
	for linea in datos2:
		archivo2.write(':'.join(linea)+'\n')
	archivo2.close()
