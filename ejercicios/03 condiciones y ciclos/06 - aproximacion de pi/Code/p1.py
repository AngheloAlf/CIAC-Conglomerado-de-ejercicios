def pi_aprox(ciclos):
    n=1
    suma=0
    while n<=ciclos:
        suma+=(1.0/((2*n)-1))*(-1)**(n+1)
        n+=1
    return suma*4