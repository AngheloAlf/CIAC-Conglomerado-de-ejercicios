n1 = raw_input("Ingrese el primer numero: ")
n2 = raw_input("Ingrese el segundo numero: ")

suma = 0
multiplicacion = 1

i = n1 + 1

while i < n2:
    suma = suma + i
    multiplicacion = multiplicacion * i
    i = i + 1

print "La suma es: ", suma
print "La multiplicacion es: ", multiplicacion
