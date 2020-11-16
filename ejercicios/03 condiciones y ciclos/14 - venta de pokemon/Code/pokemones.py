total_francis=0
total_mike=0
total_ash=0
op=raw_input('Operacion: ')
while op!='0':
    if op=='1':
        monto=int(raw_input('Ingrese pokemones vendidos: '))
        venta=raw_input('Ingrese vendedor [M:Mike, F:Francis, A:Ash]: ')
        if venta=='M':
            total_mike+=monto
        elif venta=='F':
            total_francis+=monto
        elif venta=='A':
            total_ash+=monto
    elif op=='2':
        maximo=max(total_francis,total_mike,total_ash)
        if total_francis==maximo:
            print 'El mejor es Francis, que ha vendido '+str(total_francis),'pokemones'
        elif total_mike==maximo:
            print 'El mejor es Mike, que ha vendido '+str(total_mike),'pokemones'
        elif total_ash==maximo:
            print 'El mejor es Ash, que ha vendido '+str(total_mike),'pokemones'
    op=raw_input('Operacion: ')

print 'Se vendieron',total_mike+total_francis+total_ash,'pokemones'
            
