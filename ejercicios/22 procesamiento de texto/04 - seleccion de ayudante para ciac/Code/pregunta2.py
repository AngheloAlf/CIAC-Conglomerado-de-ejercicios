alumnos=[
    'Arturito;5430.82;35,67,80,40',
    'Miguel;6341.47;92,77,84',
    'Federico;10341;0,0,1,0,7',
    'Pedrote;4500;57,68,100']

def formar_diccionario(alumnos):
    diccionario={}
    for alumno in alumnos:
        datos=alumno.split(';')
        notas=map(int,datos[2].split(','))
        promedio=round(float(sum(notas))/len(notas),1)
        diccionario[datos[0]]=(float(datos[1]),promedio)
    return diccionario

def agregar_alumno(nombre,prioridad,notas):
    linea_notas=','.join(map(str,notas))
    s='{0};{1};{2}'.format(nombre,prioridad,linea_notas)
    alumnos.append(s)
    return None

def calcular_puntaje(prioridad,promedio):
    return ((prioridad-7000)**2+(promedio-100)**2)**0.5

def seleccionar_ayudante(alumnos):
    puntaje_minimo=float('inf')
    dic_alumnos=formar_diccionario(alumnos)
    for alumno,(prioridad,promedio) in dic_alumnos.items():
        if calcular_puntaje(prioridad,promedio)<puntaje_minimo:
            puntaje_minimo=calcular_puntaje(prioridad,promedio)
            ayudante=alumno
    return ayudante
        
    
