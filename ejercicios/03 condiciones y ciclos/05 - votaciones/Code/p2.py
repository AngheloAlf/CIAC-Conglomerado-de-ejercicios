# Guia 5, pregunta 2

numero = int(raw_input('Numero de universidades: '))

i        = 0
aceptan  = 0
rechazan = 0
empate   = 0
while i < numero:
	print ''
	nombre     = raw_input('Universidad: ')
	u_aceptan  = 0
	u_rechazan = 0
	u_blancos  = 0
	u_nulos    = 0
	votacion   = True
	while votacion:
		voto = raw_input('Voto: ')
		if voto == 'X':
			votacion = False
		elif voto == 'A':
			u_aceptan += 1
		elif voto == 'R':
			u_rechazan += 1
		elif voto == 'B':
			u_blancos += 1
		elif voto == 'N':
			u_nulos += 1
		else:
			pass
	print nombre+':',               \
	  str(u_aceptan), 'aceptan,',   \
	  str(u_rechazan), 'rechazan,', \
	  str(u_blancos), 'blancos,',   \
	  str(u_nulos), 'nulos.'
	if u_aceptan == u_rechazan:
		empate += 1
	elif u_aceptan > u_rechazan:
		aceptan += 1
	elif u_rechazan > u_aceptan:
		rechazan += 1
	i += 1
print 'Universidades que aceptan:' , str(aceptan)
print 'Universidades que rechazan:', str(rechazan)
print 'Universidades con empate:'  , str(empate)
