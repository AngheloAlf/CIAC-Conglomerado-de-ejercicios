j1 = raw_input("J1 ingrese seleccion: ")
j2 = raw_input("J2 ingrese seleccion: ")

if j1 == j2:
	print "Hubo un empate":

else:
	if j1 == "piedra":
		if j2 == "papel":
			print "Gano el jugador 2"
		else:
			print "Gano el jugador 1"
	elif j1 == "papel":
		if j2 == "tijeras":
			print "Gano el jugador 2"
		else:
			print "Gano el jugador 1"
	else:
		if j2 == "piedra":
			print "Gano el jugador 2"
		else:
			print "Gano el jugador 1"
