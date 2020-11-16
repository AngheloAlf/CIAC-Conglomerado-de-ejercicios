def impuestosRecaudados(utilidades):
	impuestos = 0
	#Empresa pequena
	if utilidades < 50:
		impuestos = utilidades * 25.0/100

		if utilidades < 20:
			impuestos = impuestos * 120.0/100

	#Empresa mediana
	elif utilidades < 80:
		impuestos = utilidades * 30.0/100
		if utilidades > 70:
			impuestos = impuestos - (impuestos * 30.0/100)
		elif utilidades > 60:
			impuestos = impuestos - (impuestos * 10.0/100)

	#Empresa grande
	else:
		impuestos = utilidades * 40.0/100
		if impuestos >= 64:
			impuestos = 0

		elif impuestos > 36:
			utilidades = utilidades / 2.0

			if utilidades < 50:
				impuestos = utilidades * 25.0/100
			elif utilidades < 80:
				impuestos = utilidades * 30.0/100
			else:
				impuestos = utilidades * 40.0/100

			impuestos = impuestos * 2

	return impuestos