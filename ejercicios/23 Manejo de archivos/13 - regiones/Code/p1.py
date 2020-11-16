def extraer_zonas(zonas):
	dicc_zonas = dict()
	arch_zonas = open(zonas)
	for linea in arch_zonas:
		datos = linea.strip().replace(',',':').split(':')
		nombre_zona = datos[0]
		regiones = datos[1:]
		dicc_zonas[nombre_zona] = regiones
	arch_zonas.close()
	return dicc_zonas

def extraer_regiones(regiones):
	dicc_regiones = dict()
	arch_regiones = open(regiones)
	for linea in arch_regiones:
		datos = linea.strip().split(':')
		region = datos[0]
		datos_region = datos[1:]
		dicc_regiones[region] = datos_region
	arch_regiones.close()
	return dicc_regiones

def extraer_cantidad_habitantes(dicc_regiones,regiones_zona):
	habitantes = list()
	for region in regiones_zona:
		habitantes.append(dicc_regiones[region][2])
	return habitantes

def datos_habitantes(zonas,regiones):
	dicc_zonas = extraer_zonas(zonas)
	dicc_regiones = extraer_regiones(regiones)
	dicc_habitantes = dict()
	for zona, regiones_zona in zonas.items():
		dicc_habitantes[zona] = extraer_cantidad_habitantes(
		                                dicc_regiones,regiones_zona)
	return dicc_habitantes

# Asuma que existe esta funcion
def entero_a_romano(x):
	return str(x) #para que no haya error al probarla

def ingresar_region(zonas,regiones,nombre,habitantes,superficie,capital,
                                                    region_natural):
	dicc_zonas = extraer_zonas(zonas)
	dicc_regiones = extraer_regiones(regiones)
	#Calcular el numero de la siguiente region
	numero_region = entero_a_romano(len(dicc_regiones)+1)
	#Agregar datos a regiones
	linea_nueva_regiones = ','.join([numero_region,nombre,habitantes,
	                                    superficie,capital])
	arch_regiones = open("regiones.txt",'a')
	arch_regiones.write(linea_nueva_regiones+"\n")
	arch_regiones.close()
	#Agregar datos a zonas
	dicc_zonas[region_natural].append(numero_region)
	#Reescribir archivo zonas.
	#Da lo mismo el reemplazar el nombre hasta este paso
	arch_zonas = open(zonas,'w')
	for region_natural, regiones in dicc_zonas.items():
		linea = "{0}:{1}\n".format(region_natural,','.join(regiones))
		arch_zonas.write(linea)
	arch_zonas.close()




