# Pregunta II: Analisis de correos electronicos.

# Estructuras dadas en enunciado:
genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}

c = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net',
     'gudrun@lala.de', 'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl',
     'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl', 'dawei@hao.cn',
     'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
     'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']
     
def obtener_dominios(correos):
	dominios = set()
	for c in correos:
		dominio = c.split('@')[1]
		dominios.add(dominio)
	dominios = list(dominios)
	dominios.sort()
	return dominios
	
def contar_tld(correos):
	tld = dict()
	for c in correos:
		dominio = c.split('.')[-1]
		if dominio not in genericos:
			tld[dominio] = 0
	for c in correos:
		dominio = c.split('.')[-1]
		if dominio not in genericos:
			tld[dominio] += 1

	return tld
