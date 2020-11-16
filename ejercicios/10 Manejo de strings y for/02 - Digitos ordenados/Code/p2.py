def esta_ordenado(numero):
	numero = str(numero)

	contador = 0
	anterior = "0"
	while contador < len(numero):
		if numero[contador] >= anterior:
			anterior = numero[contador]
		else:
			return False
		contador += 1
	return True

numero = raw_input("Ingrese un numero: ")
while numero != "Fin":
	if esta_ordenado(numero):
		print "El numero", numero, "esta ordenado"
	else:
		print "El numero", numero, "no esta ordenado"
	numero = raw_input("Ingrese un numero: ")
