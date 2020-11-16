# Precio de Pisos:
# Certamen I 2011-I

print 'Bienvenido al programa: Cotizador 1.0'
print 'Porfavor ingrese el numero del departamento:'
departamento = raw_input('numero: ')

piso     = int(departamento[-3] + departamento[-2])
precio   = 0
posicion = departamento[-1]
mar      = '73'
cerro    = '04'

if departamento == '807':
	precio = 500
elif piso == 1:
	precio = 100
elif piso == 25:
	precio = 400
else:
	# encontrar si es mar o cerro
	if posicion in mar:
		precio = 245 + int(245.0*0.13)
	elif posicion in cerro:
		precio = 245 - int(245.0*0.17)
	else:
		precio = 245
print 'el precio es', precio
