# Guia 4 2016-I
# Ejercicio 1

print 'Bienvenido usuario!'
memoria = int(raw_input('ingrese cantidad de memoria RAM (GB): '))
disco   = int(raw_input('ingrese cantidad de disco duro (GB) : '))
precio  = int(raw_input('ingrese precio (pesos)              : '))

# Nota: se asumen valores naturales.
if memoria == 4:
	pMemoria = 2.0
elif memoria < 4:
	pMemoria = 1.0
else:
	pMemoria = 3.0
	
if disco >= 500 and disco <= 1000:
	pDisco = 2.0
elif disco < 500:
	pDisco = 1.0
else:
	pDisco = 3.0
	
if precio > 1000000:
	pPrecio = 1.0
elif precio < 500000:
	pPrecio = 3.0
else:
	pPrecio = 2.0 
	
puntaje = pMemoria*0.1 + pDisco*0.5 + pPrecio*0.4
print 'El puntaje del computador es ', puntaje

if puntaje > 2:
	print 'Vale la pena comprarlo!'
else:
	print 'No se sugiere comprarlo!'
