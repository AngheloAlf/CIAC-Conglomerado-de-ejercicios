grupo = {'rick':(172,10), 'daryl':(136,11), 'michonne':(80,6),
    'glenn':(73,0), 'maggie':(55,4), 'carl':(62,1),
    'tyreese':(35,0), 'carol':(17,3) }
def total(grupo):
    lista=[0.0,0.0]
    for nombre,(walkers,humanos) in grupo.items():
        lista[0]+=walkers
        lista[1]+=humanos
    return tuple(lista)

def puntaje(grupo):
    dicc={}
    t_walkers,t_humanos=total(grupo)
    for nombre,(walkers,humanos) in grupo.items():
        dicc[nombre]=round((walkers/t_walkers)+2*(humanos/t_humanos),2)
    return dicc

def ranking(grupo):
    lista=[]
    for nombre,puntos in puntaje(grupo).items():
        lista.append((puntos,nombre))
    lista.sort()
    lista.reverse()
    lista2=[]
    for puntos,nombre in lista:
        lista2.append(nombre)
    return lista2
