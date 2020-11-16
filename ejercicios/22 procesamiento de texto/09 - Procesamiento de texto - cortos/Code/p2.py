b1='hola como estas?'
b2='14,15,16,17\n'
b3='a#3#b#5#c#7'
b4='oh mira4no gracias4un dos tres'
b5='Miguel Godoy#22#4,3,12\n'

b1=set(b1.replace('?','').split())
b2=map(int,b2.strip().split(','))

lis3=b3.split('#')
b3={}
for i in range(0,6,2):
    b3[lis3[i]]=int(lis3[i+1])

lis4=b4.split('4')
b4=[]
for frase in lis4:
    frase=frase.replace(' ','')
    b4.append((frase,len(frase)))
b4=tuple(b4)

lis5=b5.strip().split('#')
b5=[]
b5.append(lis5[0].split()[0])
b5.append(int(lis5[1]))
b5.append(map(int,lis5[2].split(',')))