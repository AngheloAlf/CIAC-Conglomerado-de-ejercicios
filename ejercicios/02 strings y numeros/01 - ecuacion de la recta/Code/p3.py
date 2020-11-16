x1=float(raw_input('Ingrese x1: '))
y1=float(raw_input('Ingrese y1: '))
x2=float(raw_input('Ingrese x2: '))
y2=float(raw_input('Ingrese y2: '))
pendiente=round((y2-y1)/(x2-x1),2)
intercepto=round(-x1*pendiente+y1,2)
print 'Pendiente:',pendiente
print 'Intercepto:',intercepto
print 'La ecuacion principal es: y = '+str(pendiente)+' x + '+str(intercepto)