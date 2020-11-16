horaActual = int(raw_input("Ingrese la hora actual: "))
horasMas = int(raw_input("Ingrese cantidad de horas: "))

dias = (horaActual + horasMas)/24
horaFutura = (horaActual + horasMas)%24

print "Son", dias, "dias, y seran las", horaFutura