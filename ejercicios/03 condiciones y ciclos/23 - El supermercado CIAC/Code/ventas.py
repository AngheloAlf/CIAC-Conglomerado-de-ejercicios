cont_paolo=0
cont_miguel=0
cont_anghelo=0
print '1. Ingresar venta'
print '2. Mejor vendedor'
print '3. Resumen diario'
print '4. Salir'
print ''
op=raw_input('Ingrese opcion: ')
while op!='4':
    if op=='1':
        vendedor=raw_input('Ingrese nombre vendedor [Miguel/Anghelo/Paolo]: ')
        venta=int(raw_input('Ingrese monto vendido: '))
        if vendedor=='Miguel':
            cont_miguel+=venta
        elif vendedor=='Anghelo':
            cont_anghelo+=venta
        elif vendedor=='Paolo':
            cont_paolo+=venta
    elif op=='2':
        mejor=max(cont_paolo,cont_miguel,cont_anghelo)
        if mejor==cont_paolo:
            print 'El mejor vendedor es Paolo, que ha vendido $'+str(cont_paolo)
        elif mejor==cont_miguel:
            print 'El mejor vendedor es Miguel, que ha vendido $'+str(cont_miguel)
        else:
            print 'El mejor vendedor es Anghelo, que ha vendido $'+str(cont_anghelo)
    elif op=='3':
        print 'Hoy se han vendido $'+str(cont_paolo+cont_miguel+cont_anghelo)
        print 'Buenas noches!'
        cont_paolo=0
        cont_miguel=0
        cont_anghelo=0
    op=raw_input('Ingrese opcion: ')
        
