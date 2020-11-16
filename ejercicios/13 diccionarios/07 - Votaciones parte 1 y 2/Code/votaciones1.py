votaciones={'Pablo':1,'Tomas':0,'Carlos':1,'Pedrito':0,'Jaimito':1}

def separar_nombres(votaciones):
    afirmativo=[]
    negativo=[]
    for nombre, valor in votaciones.items():
        if valor==1:
            afirmativo.append(nombre)
        elif valor==0:
            negativo.append(nombre)
    return (afirmativo,negativo)


def porcentaje_si(votaciones):
    afirmativo,negativo=separar_nombres(votaciones)
    return (float(len(afirmativo))*100)/(len(afirmativo)+len(negativo))

def se_acepta(votaciones):
    return porcentaje_si(votaciones)>50
