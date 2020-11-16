def filtro_altura_nombre(montanas):
    lista=[]
    for nombre,altura,inicio,fin in montanas:
        lista.append((altura,nombre))
    lista.sort()
    return lista

def duracion(inicio,fin):
    hi,mi=inicio
    hf,mf=fin
    diferencia=hf*60+mf-hi*60-mi
    return (diferencia/60,diferencia%60)

altura_max=-float('inf')
for nombre,altura,inicio,fin in montanas:
    if altura>altura_max:
        altura_max=altura
        montana_alta=nombre
        tiempo=duracion(inicio,fin)
print 'La montana mas alta que escalaron fue',montana_alta+'.'
print 'Esta tenia una altura de',altura_max,'metros.'
print 'Se demoraron',tiempo[0],'horas y',tiempo[1],'minutos.'