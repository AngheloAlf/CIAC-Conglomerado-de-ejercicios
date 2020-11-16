flota1= {
    'goleta':[('B',2),('B',3)],
    'fragata':[('B',6),('C',6),('D',6)],
    'corbeta':[('F',3),('F',4),('F',5),('F',6)] }

def actualizar_flota(flota,posicion):
    nuevo_estado_barco=[]
    for barco,posiciones in flota.items():
        if posicion in posiciones:
            for posicion1 in posiciones:
                if posicion != posicion1:
                    nuevo_estado_barco.append(posicion1)
            flota[barco]=nuevo_estado_barco

def actualizar_flota2(flota,posicion):
    for barco,posiciones in flota.items():
        if posicion in posiciones:
            flota[barco].remove(posicion)

def estado_actual(flota):
    porcentajes={}
    for barco,posiciones in flota.items():
        if barco=='goleta':
            porcentaje =(len(posiciones)*100)/2
        elif barco=='fragata':
            porcentaje =(len(posiciones)*100)/3
        elif barco=='corbeta':
            porcentaje=(len(posiciones)*100)/4
        porcentajes[barco]= porcentaje
    return porcentajes
