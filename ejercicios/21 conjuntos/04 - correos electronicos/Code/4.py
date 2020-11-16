def dominios(correos):
    dominios=set()
    for correo in correos:
        s=''
        letraEnDominio=False
        for letra in correo:
            if letraEnDominio:
                s+=letra
            if letra=='@':
                letraEnDominio=True
        dominios.add(s)
    return dominios

def total(correos,seImprime):
    diccionario={}
    total_global=0
    for correo,(rec,env) in correos.items():
        diccionario[correo]=rec+env
        total_global+=rec+env
    if seImprime:
        print 'Correos totales: ',total_global
    return diccionario

def mayorUso(correos):
    maximo=-float('inf')
    for correo,cantidad in total(correos,False).items():
        if cantidad>maximo:
            mayor_usuario=correo
            maximo=cantidad
    return mayor_usuario