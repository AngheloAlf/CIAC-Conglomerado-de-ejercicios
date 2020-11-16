mapa = {
	'A': {'B','C'},
	'B': {'A','D','E','G'},
	'C': {'A','D'},
	'D': {'B','C','E','G','F'},
	'E': {'B','D','G'},
	'F': {'D'},
	'G': {'E','B','D'}
}

# Funcion apartado a):
def son_vecinas(mapa, p, q):
	
	vecinos_p = mapa[p]
	vecinos_q = mapa[q]
	
	if p in vecinos_q:
		return True
	if q in vecinos_p:
		return True
	return False
	
# Funcion apartado b):	
def tienen_vecino_en_comun(mapa, p, q):
	
	vecinos_p = mapa[p]
	vecinos_q = mapa[q]
	inter     = vecinos_p & vecinos_q
	
	if len(inter) > 0:
		return True
	else:
		return False
		
# Funcion apartado c):
def existe_ruta(mapa, ruta):
	
	for i in range(len(ruta)-1):
		p = ruta[i]
		q = ruta[i+1]
		if not(son_vecinas(mapa, p, q)):
			return False
	return True
