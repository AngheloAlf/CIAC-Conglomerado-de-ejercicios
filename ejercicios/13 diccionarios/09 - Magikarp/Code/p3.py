def agregarMagikarp(id, nombre, largo, alto, peso, nivel):
    dimensiones = (largo, alto, peso)
    tamano[id] = dimensiones
    niveles[id] = nivel
    nombres[nombre] = id

def quitarMagikarp(id):
    del tamano[id]
    del niveles[id]
    for nombre, id2 in nombres.items():
        if id2 == id:
            del nombres[nombre]
            break

def invertirNombres(nombres):
    nomb2 = dict()
    for nom, id in nombres:
        nomb2[id] = nom
    return nomb2

def mostrarMagikarps():
    nombDict = invertirNombres(nombres)
    magikarps = list()
    for id in tamano.keys():
        nom = nombDict[id]
        tam = nombres[id]
        niv = niveles[id]
        tupla = (nom, tam, niv)
        magikarps.append(tupla)
    return magikarps

def actualizarMagikarp(id, nombre, largo, alto, peso, nivel):
    quitarMagikarp(id)
    agregarMagikarp(id, nombre, largo, alto, peso, nivel)

def puntaje(dimensiones, nivel):
    l, a, p = dimensiones
    return (l * a * p)/float(nivel)

def contarMejores(puntajeMax):
    contadorMayor = 0
    contadorMenor = 0
    for id in tamano.keys():
        dimensiones = tamano[id]
        nivel = niveles[id]
        punt = puntaje(dimensiones, nivel)
        if punt > puntajeMax:
            contadorMayor += 1
        else:
            contadorMenor += 1
    return contadorMayor, contadorMenor

def mejorMagikarp():
    nombDict = invertirNombres(nombres)
    magi = dict()
    for id in tamano.keys():
        dimensiones = tamano[id]
        nivel = niveles[id]
        punt = puntaje(dimensiones, nivel)
        if punt not in magi:
            magi[punt] = list()
        magi[punt].append(nombDict[id])

    mayor = -float("inf")
    nombreMejor = list()
    for punt, noms in magi.items():
        if punt > mayor:
            mayor = punt
            nombreMejor = noms

    return noms

while True:
    print "1: Agregar Magikarp"
    print "2: Quitar Magikarp"
    print "3: Mostrar Magikarps"
    print "4: Actualizar Magikarps"
    print "5: Contar a los mejores Magikarps"
    print "6: Buscar mejores Magikarps"
    print "Cualquier otra cosa: Salir"
    opcion = raw_input("Ingrese opcion: ")
    if opcion == "1":
        id = raw_input("Ingrese ID: ")
        nombre = raw_input("Ingrese nombre: ")
        largo = int(raw_input("Ingrese largo: "))
        alto = int(raw_input("Ingrese alto: "))
        peso = int(raw_input("Ingrese peso: "))
        nivel = int(raw_input("Ingrese nivel: "))
        agregarMagikarp(id, nombre, largo, alto, peso, nivel)
    elif opcion == "2":
        id = raw_input("Ingrese ID: ")
        quitarMagikarp(id)
    elif opcion == "3":
        print mostrarMagikarps()
    elif opcion == "4":
        id = raw_input("Ingrese ID: ")
        nombre = raw_input("Ingrese nombre: ")
        largo = int(raw_input("Ingrese largo: "))
        alto = int(raw_input("Ingrese alto: "))
        peso = int(raw_input("Ingrese peso: "))
        nivel = int(raw_input("Ingrese nivel: "))
        actualizarMagikarp(id, nombre, largo, alto, peso, nivel)
    elif opcion == "5":
        punt = int(raw_input("Ingrese puntaje: "))
        print contarMejores(punt)
    elif opcion == "6":
        mejorMagikarp()
    else:
        break