usuarios=[
    ('Miguel','masculino',['musica','programacion','breaking bad'],4),
    ('Chavo del 8','masculino',['tortas de jamon','enojar a Don Ramon'],3),
    ('Rupertina','femenino',['campo','MCC','Ruperto'],6),
    ('Walter White','masculino',['cocina','metanfetamina','quimica'],2),
    #...
    ]

def filtro_por_genero(genero,usuarios):
    lista=[]
    for usuario in usuarios:
        nombre,genero1,intereses,likes=usuario
        if genero==genero1:
            lista.append((nombre,intereses))
    return lista

def filtro_por_interes(intereses,usuarios):
    lista=[]
    for interes in intereses:
        for nombre,gene,intereses1,likes in usuarios:
            if interes in intereses1:
                lista.append((nombre,intereses1))
    return lista

def dar_like(nombre,usuarios):
    for usuario in usuarios:
        nom,gene,intereses,likes=usuario
        if nom==nombre:
            indice=usuarios.index(usuario)
            usuarios[indice]=nom,gene,intereses,likes+1
    return None