SansaVuelos = {
# codigo: (nombre, partida, destino, escalas, tiempo_promedio),
'NH217': ('All Nippon Airways','Tokyo','Santiago', ['Atlanta'],1620),
'AY154': ('Finnair','Helsinki','Moscu', ['Riga'], 175),
'OV171': ('Estonian Air','Tallin','Paris', ['Amsterdam','Berlin'], 205)}

Vuelo = {
# identificador: codigo, fecha
3542: ('AY154', (2013,12,25)),
6433: ('NH217', (2013,12,31)),
1313: ('NH217', (2013,11,6)),
}

# Funcion apartado a):
def vuelos_entre_fechas(fecha1,fecha2,Vuelo):
	# Variables:
	vuelos_entre = set()
	
	# Procedimiento:
	for registros in Vuelo.values():
		if (fecha1 <= registros[1]) and (registros[1] <= fecha2):
			vuelos_entre.add(registros[0])
	return vuelos_entre
	
# funciones auxiliares:
def tres_o_mas(vuelo):
	# vuelo: (nombre, partida, destino, escalas, tiempo_promedio)
	# Variables:
	lista_escalas  = vuelo[3]
	numero_escalas = len(lista_escalas) 
	
	# Procedimiento:
	if numero_escalas >= 3:
	    return True
	else:
		return False

def viaje_agotador(vuelo):
	# Variables:
	duracion = vuelo[4]
	criterio = 8*60
	
	# Procedimiento:
	if duracion >= criterio:
		return True
	else:
		return False

# Funcion apartado b):
def vuelos_agotadores(fecha1,fecha2,Vuelos, SansaVuelos):
	# Variables:
	agotadores   = set()
	escalas      = 0
	tiempo_viaje = 0
	vuelo        = None
	
	# Procedimiento:
	for registros in Vuelos.values():
		vuelo        = registros[0]
		escalas      = tres_o_mas(SansaVuelos[vuelo])
		tiempo_viaje = viaje_agotador(SansaVuelos[vuelo])
		if escalas or tiempo_viaje:
			agotadores.add(registros[0])
	return agotadores

# Funcion apartado c):	
def vuelos(partida, destino, Vuelo, SansaVuelos):
	# Variables:
	seleccionados = list()
	temp_origen   = None
	temp_destino  = None
	criterio      = None
	temp_sel      = None
	
	# Procedimiento:
	for registros in Vuelo.values():
		temp_origen  = SansaVuelos[registros[0]][1]
		temp_destino = SansaVuelos[registros[0]][2]
		criterio = \
		    (temp_origen  == partida) and \
		    (temp_destino == destino)
		if criterio:
			temp_sel = \
			    (registros[0], \
			     SansaVuelos[registros[0]][0], \
			     registros[1])
			seleccionados.append(temp_sel)
	return seleccionados
