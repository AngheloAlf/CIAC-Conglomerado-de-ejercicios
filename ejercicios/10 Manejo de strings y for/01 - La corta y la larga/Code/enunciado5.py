n = 54321
cont = 2
suma = 0
while n > 0:
	dig = n % 10
	if cont == 5:
		cont = 2
	suma = suma + dig * cont
	n = n/10
	cont = cont + 1
d = suma % 11
r = 11 - d
if r == 10:
	dv = 'k'
elif r == 11:
	dv = 0
else:
	dv = r
print dv
