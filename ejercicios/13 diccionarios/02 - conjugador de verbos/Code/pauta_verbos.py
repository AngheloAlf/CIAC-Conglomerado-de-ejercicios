pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

declinaciones={'ar':['o','as','a','amos','ais','an'],
       'er':['o','es','e','emos','eis','en'],
       'ir':['o','es','e','imos','is','en']}

verbo=raw_input('Ingrese verbo: ')
base=verbo[:-2:]
terminacion=verbo[-2:]
for i in range(6):
    print pronombres[i]+' '+base+declinaciones[terminacion][i]
    
    
