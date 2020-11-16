# Pregunta I: Funciones para Procesar Texto.

vocales = {'a': 'i', 'e': 'u', 'i': 'a', 'o':'e', 'u':'o'}

def cifrar_texto(texto, tabla):
    temp = list()
    for i in texto:
		if i in 'aeiou':
			i = tabla[i]
		temp.append(i)
	
    return ''.join(temp)

Tabla = {
         'moneda': 'calabaza',
         'pablo' : 'estrecho',
         'botin' : 'servilleta',
         'robo'  : 'abrazo'}

def cifrar_palabras(texto, tabla):
	for i in tabla.keys():
		texto = texto.replace(i, tabla[i])
	return texto

receptores =  [('Pedro', 'Hernandez'),
               ('Pietro', 'Morales'),
               ('Sandro', 'Maureira')]

def envios_codificados(texto, receptores, tablavocal, tabla):
	lista = list()
	base  = 'Estimado {nombre}, {apellido}. '
	texto = cifrar_palabras(texto, Tabla)
	texto = cifrar_texto(texto, vocales)
	
	for a, b in receptores:
		temp = base
		temp = temp.format(nombre = a, apellido = b)
		lista.append(temp + texto)
	return lista
