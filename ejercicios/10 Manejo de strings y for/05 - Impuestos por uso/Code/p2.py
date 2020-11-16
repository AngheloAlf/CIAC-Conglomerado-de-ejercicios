total = 0

pregunta = "Si"

while pregunta != "No":
	dia = raw_input("Dia de la semana: ")
	horaEntrada = int(raw_input("Hora de entrada: "))
	minutoEntrada = int(raw_input("Minuto de entrada: "))
	horaSalida = int(raw_input("Hora de salida: "))
	minutoSalida = int(raw_input("Minuto de salida: "))

	minutos = horaSalida*60+minutoSalida -horaEntrada*60 -minutoEntrada
	horas = minutos/60

	evaluacion = raw_input("Tiene evaluacion al dia siguiente?: ")

	if dia == "Sabado" or dia == "Domingo":
		cobro = horas*100
		total += cobro
		print "El estudiante debe pagar $", cobro

	else:
		if horaSalida < 7:
			cobro = horas * 200
		else:
			minutos = (7*60 - (horaEntrada*60 + minutoEntrada))/60
			cobro = minutos * 200
		print "El estudiante debe pagar $", cobro
		total += cobro

	pregunta = raw_input("Quiere ingresar otro estudiante?: ")

print "El total obtenido es: $", total
