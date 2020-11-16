puntos=[
    (101.86,273),(109.26,293),(112.59,303),
    (116.11,313),(119.56,323),(123.07,333)
    ]
    
def suma_x(puntos):
    suma=0.0
    for x,y in puntos:
        suma+=x
    return suma
def suma_y(puntos):
    suma=0.0
    for x,y in puntos:
        suma+=y
    return suma
def prod_punto(puntos): #(suma de x*y)
    suma=0.0
    for i in range(len(puntos)):
        x,y=puntos[i]
        suma+=x*y
    return suma
def suma_x_cuadrado(puntos):
    suma=0.0
    for x,_ in puntos:
        suma+=x**2
    return suma
def promedios(puntos):
    suma_x=0.0
    suma_y=0.0
    for x,y in puntos:
        suma_x+=x
        suma_y+=y
    return suma_x/len(puntos),suma_y/len(puntos)
n=len(puntos)
a_numerador=n*prod_punto(puntos) - suma_x(puntos)*suma_y(puntos)
a_denominador=n*suma_x_cuadrado(puntos)-(suma_x(puntos)**2)
a=a_numerador/a_denominador
b=promedios(puntos)[1]- a*promedios(puntos)[0]

print_1='La regresion lineal de los puntos es: y = '+str(round(a,2))
print_2='x + '+str(round(b,2))
print print_1+print_2


        