def contar_letras(palabra):
	dic={}
	for letra in palabra.lower():
		if letra not in dic:
			dic[letra]=0
		dic[letra]+=1
	return dic

def son_anagramas(p1,p2):
    letras1=contar_letras(p1)
    letras2=contar_letras(p2)
    return letras1==letras2

def es_panvocalica(palabra):
	vocales=set()
	for letra in palabra.lower():
		if letra in 'aeiou':
			vocales.add(letra)
	return vocales==set('aeiou')

    
def en_orden(palabra):
    for i in range(len(palabra)-1):
        if palabra[i]>palabra[i+1]:
            return False
    return True

def en_orden_segun(palabra,guia):
    for i in range(len(guia)-1):
        if palabra.index(guia[i])>palabra.index(guia[i+1]):
            return False
    return True

def palabras_repetidas(oracion):
    oracion=oracion.lower().split()
    palabras=set(oracion)
    repetidas=[]
    for palabra in palabras:
        if oracion.count(palabra)>1:
            repetidas.append(palabra)
    return repetidas
