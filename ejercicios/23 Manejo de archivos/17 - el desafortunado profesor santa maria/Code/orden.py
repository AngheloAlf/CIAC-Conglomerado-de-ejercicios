def crea_archivo():
	file_alumnos_1=open("alumnos_1.txt")
	file _sangre=open("sangre.txt","w")
	for linea_raw_1 in file_alumnos_1:
		linea_1=linea_raw_1.strip().split(';')
		file_alumnos_2=open('alumnos_2.txt')
		for linea_raw_2 in file_alumnos_2:
			linea_2=linea_raw_2.strip().split(';')
			if linea_1[1]==linea_2[0]:
				datos_1=linea_1[1]+';'+linea_1[2]+';'
				file_sangre.write(datos_1+linea_2[1]+'\n')
		file_alumnos_2.close()
	file_alumnos_1.close()
	file_sangre.close()
	return

