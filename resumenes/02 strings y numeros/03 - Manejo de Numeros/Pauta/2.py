#Ejercicio 1
num_1=float(raw_input('Ingrese primer numero: '))
num_2=float(raw_input('Ingrese segundo numero: '))
num_3=float(raw_input('Ingrese tercer numero: '))
promedio=(num_1+num_2+num_3)/3.0
print 'El promedio de los numeros es',round(promedio,3)

#Ejercicio 2
hora_1=int(raw_input('Ingrese las horas actuales: '))
min_1=int(raw_input('Ingrese los minutos actuales: '))
hora_2=int(raw_input('Ingrese las horas siguientes: '))
min_2=int(raw_input('Ingrese los minutos siguientes: '))

restante=(hora_2*60+min_2)-(hora_1*60+min_1)
h_restante=restante/60
m_restante=restante%60

parte_1='Son las '+str(hora_1)+':'+str(min_1)
parte_2=' y para que sean las '+str(hora_2)+':'+str(min_2)
parte_3=' queda '+str(h_restante)+':'+str(m_restante)

print parte_1+parte_2+parte_3