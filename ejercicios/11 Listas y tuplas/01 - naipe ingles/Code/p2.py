# Ejercicio 2
from random import choice

# 1)
def nueva_baraja():
	baraja = list()
	Palos   = ['pica', 'trebol', 'corazon', 'diamante']
	for p in Palos:
		for n in range(13):
			numero = str(n+1)
			if numero == '11':
				numero = 'j'
			elif numero == '12':
				numero = 'q'
			elif numero == '13':
				numero = 'k'
			baraja.append((p, numero))  
	return baraja
			
# 2)
def robar(baraja):
	carta = baraja[0]
	del baraja[0]
	return carta
	
# 3)
def barajar(baraja):
	nueva = list()
	for i in range(len(baraja)):
		switch = True
		while switch:
			carta = choice(baraja)
			if carta not in nueva:
				nueva.append(carta)
				switch = False
	return nueva
	
# 4)
def entregar_mano(baraja, cartas):
	mano = list()
	for i in range(cartas):
		palo, numero = robar(baraja)
		mano.append((palo, numero))
	return mano	

# prueba:
jugadores  = int(raw_input('Ingrese numero de jugadores: '))
cartasMano = int(raw_input('Ingrese numero cartas por mano: '))
baraja = nueva_baraja()
for i in range(jugadores):
	baraja = barajar(baraja)
	mano = entregar_mano(baraja, cartasMano)
	print 'mano jugador ' + str(i+1) + ':'
	picas, corazon, diamantes, trebol = 0, 0, 0, 0
	for p, n in mano:
		if p == 'trebol':
			trebol += 1
		elif p == 'corazon':
			corazon += 1
		elif p == 'pica':
			picas += 1
		else:
			diamantes += 1
	print 'picas:', picas
	print 'corazon:', corazon
	print 'diamante:', diamantes
	print 'trebol:', trebol
