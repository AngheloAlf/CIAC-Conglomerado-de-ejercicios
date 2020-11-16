ruta=raw_input('Ruta: ')
eje_y=0
eje_x=0
cont=0
while cont<len(ruta):
    if ruta[cont]=='n':
        eje_y+=1
    elif ruta[cont]=='s':
        eje_y-=1
    elif ruta[cont]=='o':
        eje_x-=1
    elif ruta[cont]=='e':
        eje_x+=1
    cont+=1
opt=''
if eje_x>0:
    opt+='e'*eje_x
else:
    opt+='o'*(eje_x*-1)
if eje_y>0:
    opt+='n'*eje_y
else:
    opt+='s'*(eje_y*-1)
print 'Ruta optimizada:',opt
        
