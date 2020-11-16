# Guia 5, pregunta I

print '***************************************'
print '* Bienvenido al sistema de evaluacion *'
print '* Programacion de Computadores I      *'
print '***************************************'

condicion = True
while condicion:
  print 'Opciones:'
  print '1) Ingresar Alumno'
  print '2) Salir'
  alternativa = int(raw_input('Que desea hacer?: '))
  
  if alternativa == 2:
    condicion = False
    print 'Adios!'
  elif alternativa == 1:
	nombre   = raw_input('Nombre alumno: ')
	c1       = float(raw_input('Nota C1: '))
	c2       = float(raw_input('Nota C2: '))
	c3       = float(raw_input('Nota C3: '))
	c4       = float(raw_input('Nota C4: '))
	promedio = int(round(c1*0.2 + c2*0.2 + c3*0.3 + c4*0.3))
	if promedio >54:
		print 'El alumno', nombre, \
		  'aprobo con', promedio, 'en promedio'
	else:
		print 'El alumno', nombre, \
		  'reprobo con', promedio, 'en promedio'
  else:
	print 'Error: Alternativa no valida'
