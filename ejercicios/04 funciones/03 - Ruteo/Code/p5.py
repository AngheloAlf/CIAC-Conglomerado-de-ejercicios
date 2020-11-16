def numero_a_binario(numero):
	total = ""
	while numero != 0:
		resto = numero % 2
		total += str(resto)
		numero = numero / 2
	return total[::-1]



print numero_a_binario(25)
print numero_a_binario(6)