def listar_bajas(rango,registro,bajas):                                 
    arch1=open(registro)                                                
    lista_soldados=[]                                                   
    for linea in arch1:                                                 
        soldado=linea.strip().split(',')                                
        if soldado[1]==rango:                                           
            lista_soldados.append(tuple(soldado[0].strip().split(':'))) 
    arch1.close()                                                       
    c=0                                                                 
    d=0
    for baja in bajas:
        if bajas[c]:
            del lista_soldados[d]                                       
            d-=1
        d+=1
        c+=1
    return lista_soldados                                               

def promedio_edad(bajas):
    suma=0                                                              
    for baja in bajas:                                                  
        suma+=int(baja[1])                                              
    return round(float(suma)/len(bajas),1)                              
            
def actualizar_registro(registro,bajas):
    arch1=open(registro)                                                
    arch2=open('nuevo_escuadron.txt','w')                               
    for linea in arch1:                                                 
        soldado=tuple(linea.strip().split(',')[0].split(':'))           
        if soldado not in bajas:                                        
            arch2.write(linea)                                          
    arch1.close()                                           
    arch2.close()                                                       
    return None
