def formar_diccionario(archivo):
    diccionario={}
    arch=open(archivo)
    for linea in arch:
        datos=linea.strip().split(';')
        notas=map(int,datos[2].split(','))
        promedio=round(float(sum(notas))/len(notas),1)
        diccionario[datos[0]]=(float(datos[1]),promedio)
    arch.close()
    return diccionario

def agregar_alumno(nombre,prioridad,notas,archivo):
    arch=open(archivo,'a')
    linea_notas=','.join(map(str,notas))
    s='{0};{1};{2}\n'.format(nombre,prioridad,linea_notas)
    arch.write(s)
    arch.close()
    return None

def modificar_alumno(nombre,prioridad,notas,archivo):
    original=open(archivo)
    temporal=open('temp.txt','w')
    for linea in original:
        if nombre in linea:
            linea_notas=','.join(map(str,notas))
            f='{0};{1};{2}\n'.format(nombre,prioridad,linea_notas)
            temporal.write(f)
        else:
            temporal.write(linea)
    original.close()
    temporal.close()
    original=open(archivo,'w')
    temporal=open('temp.txt')
    for linea in temporal:
        original.write(linea)
    original.close()
    temporal.close()
    return None

def calcular_puntaje(prioridad,promedio):
    return ((prioridad-7000)**2+(promedio-100)**2)**0.5

def seleccionar_ayudante(archivo):
    puntaje_minimo=float('inf')
    dic_alumnos=formar_diccionario(archivo)
    for alumno,(prioridad,promedio) in dic_alumnos.items():
        if calcular_puntaje(prioridad,promedio)<puntaje_minimo:
            puntaje_minimo=calcular_puntaje(prioridad,promedio)
            ayudante=alumno
    return ayudante



