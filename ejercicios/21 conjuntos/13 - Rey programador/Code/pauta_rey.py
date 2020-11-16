hijos = {
'Tywin': set(['Tyron', 'Jaime', 'Cersei']),
'Jaime': set(['Joffrey', 'Myrcella', 'Tommen','Miguel']),
'Cersei': set(['Joffrey', 'Myrcella', 'Tommen','Miguel']),
'Eddard': set(['Robb', 'Sansa', 'Arya', 'Brandon', 'Rickon', 'Jon']),
'Catelyn': set(['Robb', 'Sansa', 'Arya', 'Brandon', 'Rickon']),
# ...
}

muertos = set(['Tywin', 'Tommen','Myrcella'])

def todos(hijos):
    conj=set()
    for llave,valor in hijos.items():
        conj.add(llave)
        conj=conj|valor
    return conj

def los_papis(hijos):
    papis={}
    for hijo in todos(hijos):
        for llave,valor in hijos.items():
            if hijo in valor:
                if hijo not in papis:
                    papis[hijo]=set()
                papis[hijo].add(llave)
    return papis

def ascendencia(persona):
    lista=[]
    if persona not in los_papis(hijos):
        return 1
    for i in los_papis(hijos)[persona]:
        lista.append(1+ascendencia(i))
    return max(lista)
    

def candidatos(hijos, muertos):
    mejor_ascendencia=-float('inf')
    conj_mejor=set()
    for hijo in todos(hijos):
        if ascendencia(hijo)>mejor_ascendencia:
            mejor_ascendencia=ascendencia(hijo)
            conj_mejor=set()
        if ascendencia(hijo)==mejor_ascendencia:
            conj_mejor.add(hijo)
    return list(conj_mejor-muertos)
