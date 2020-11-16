def digito_verificador(numero):
    contador=0
    parcial=0
    for i in numero[::-1]:
        parcial+=int(i)*((contador%6)+2)
        contador+=1
    parcial%=11
    parcial=11-parcial
    if parcial==11:
        return '0'
    elif parcial==10:
        return 'K'
    else:
        return str(parcial)

numero=raw_input('Ingrese numero: ')
print 'El RUT es '+numero+'-'+digito_verificador(numero)