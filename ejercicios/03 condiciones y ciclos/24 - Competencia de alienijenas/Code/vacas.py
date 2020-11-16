maximo=-float('inf')
total=0
nombre=raw_input('Nombre del alien: ')
while nombre!='0':
    cantidad=int(raw_input('Numero de vacas extraidas: '))
    total+=cantidad
    if cantidad>maximo:
        mejor_alien=nombre
        maximo=cantidad
    nombre=raw_input('Nombre del alien: ')

print 'El total de vacas liberadas fue: '+str(total)
print 'El mejor alien fue',mejor_alien,'que libero',maximo,'vacas'
