hora1=int(raw_input('Ingrese entrada (en horas):'))
min1=int(raw_input('Ingrese entrada (en minutos):'))
hora2=int(raw_input('Ingrese salida (en horas):'))
min2=int(raw_input('Ingrese salida (en minutos):'))

minutos=hora2*60+min2-hora1*60-min1
if minutos>120:
    cobro=15*minutos
else:
    cobro=25*minutos
horas=minutos/60
minutos%=60

print 'Usted estuvo',horas,'horas y',minutos,'minutos'
print 'Me debes $'+str(cobro)



