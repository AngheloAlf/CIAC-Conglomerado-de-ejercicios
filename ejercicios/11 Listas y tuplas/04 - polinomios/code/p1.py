# Ejercicio I. Polinomios
# CIAC. 2016-II

def grado(p):
	
	return len(p) - 1
	
def evaluar(p, x):
	
	valor = 0
	i     = 0
	while i < len(p):
		valor += p[i]*x**i
		i += 1
	return valor
	
def sumar_polinomios(p1, p2):
	
	suma = list()
	g1   = grado(p1)
	g2   = grado(p2)
	d    = g2 - g1
	if d > 0:
		for i in range(d):
			p1.append(0)
	else:
		for i in range(abs(d)):
			p2.append(0)
			
	i = 0
	while i < len(p1):
		suma.append(p1[i] + p2[i])
		i += 1
	return suma
	
def derivar_polinomio(p):
	
	derivada = list()
	
	i = 1
	while i < len(p):
		derivada.append(p[i]*i)
		i += 1
	return derivada

def multiplicar_polinomios(p1, p2):
	
	prod = list()
	g1   = grado(p1)
	g2   = grado(p2)
	p    = g1 + g2
	d1   = p - g1
	d2   = p - g2
	
	print p
	for i in range(d1):
			p1.append(0)
	for i in range(d2):
			p2.append(0)
	n = 0
	while n < len(p1):
		suma_temp = 0
		k         = 0
		while k <= n:
			suma_temp += p1[k]*p2[n-k]
			k += 1
		prod.append(suma_temp)
		n += 1
	return prod
