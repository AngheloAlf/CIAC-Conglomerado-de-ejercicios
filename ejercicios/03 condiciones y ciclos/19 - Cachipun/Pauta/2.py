a = float(raw_input("Ingrese a: "))
b = float(raw_input("Ingrese b: "))
c = float(raw_input("Ingrese c: "))

x0 = -b / (2 * a)
y0 = a*x0**2 + b*x0 + c

print ""
print "El punto vertice de la ecuacion es (" + str(x0) + ", " + str(y0) + ")"

discriminante = b**2 - 4*a*c

if discriminante > 0:
	discriminante = discriminante**0.5
	raiz1 = (-b + discriminante) / (2 * a)
	raiz2 = (-b - discriminante) / (2 * a)
	print "Las raices de la ecuacion son: "+str(raiz1)+" y "+str(raiz2)
elif discriminante == 0:
	raiz = -b / (2 * a)
	print "La raiz de la ecuacion es: " + str(raiz)
else:
	print "La ecuacion no tiene raices en los reales"

print "La ecuacion cuadratica es: "+str(a)+"x^2 + "+str(b)+"x + "+str(c)
