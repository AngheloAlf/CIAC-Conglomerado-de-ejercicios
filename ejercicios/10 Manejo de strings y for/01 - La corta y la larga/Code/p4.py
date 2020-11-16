def binario_a_numero(binario):
	binario_invertido = binario[::-1]
	i = 0
	total = 0
	potencia  = 0
	while i < len(binario_invertido):
		numerito = int(binario_invertido[i])
		multiplicado = numerito * (2 ** potencia)
		total = total + multiplicado
		potencia += 1
		i += 1
	return total
