ingresarMas = "Si"
aceptan = 0
rechazan = 0
blancos = 0
nulos = 0
CEE = 0
total = 0

while ingresarMas != "No":
	votos = raw_input("Ingrese votos:")
	i = 0
	while i < len(votos):
		votoUnico = votos[i]
		if votoUnico == "A":
			aceptan += 1
		elif votoUnico == "R":
			rechazan += 1
		elif votoUnico == "B":
			blancos += 1
		else:
			nulos += 1
		total += 1

	CEE += 1

	ingresarMas = raw_input("Ingresara mas votos?: ")

print "Se ingresaron", total, "votos"
print "Aceptan:", aceptan, ", es decir", aceptan*100.0/total, "%"
print "Rechazan:", rechazan, ", es decir", rechazan*100.0/total, "%"
print "Blancos:", blancos, ", es decir", blancos*100.0/total, "%"
print "Nulos:", nulos, ", es decir", nulos*100.0/total, "%"
print "Se ingresaron los votos de", CEE, "centros de estudiantes"