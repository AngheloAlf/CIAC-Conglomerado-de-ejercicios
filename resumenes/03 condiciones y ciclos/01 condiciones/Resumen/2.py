#Entrada de datos
nota1 = int( raw_input("Ingrese Nota 1: ") )
nota2 = int( raw_input("Ingrese Nota 2: ") )
nota3 = int( raw_input("Ingrese Nota 3: ") )

#Proceso				   Recordar que generalmente buscamos
promedio = (nota1 + nota2 + nota3) / 3.0 # la division real y no entera
					 # [1/2 == 0]

if promedio > 55:
  #Salida 1
  print "¡Aprobado!"
else:
  #Salida 2
  print "¡Casi!"