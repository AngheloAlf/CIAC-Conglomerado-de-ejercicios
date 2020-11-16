def promedioPersonasCalle(censo):
    promedio = dict()
    for calle, casas in censo.items():
        #promedio[calle] = [cantidad_personas, cantidad_casas]
        promedio[calle] = [0, 0]
        for numero, datos in casas.items():
            cencista, numero_personas, edades = datos
            if numero_personas != 0:
                promedio[calle][0] += numero_personas
                promedio[calle][1] += 1

    promedioCalculado = dict()
    for calle in promedio:
        cantidad_personas, cantidad_casas = promedio[calle]
        if cantidad_casas == 0:
            promedioCalculado[calle] = 0.0
        else:
            promedioCalculado[calle] = cantidad_personas / cantidad_casas

    return promedioCalculado


def porcentajePagar(censo, cencistas):
    porcentajesCencistas = dict()
    for censador, casas_total_censador in cencistas.items():
        casasCensadas = 0.0
        for calle, casas in censo.items():
            for numero, datos in casas.items():
                cencista, numero_personas, edades = datos
                if censador == cencista:
                    casasCensadas += 1.0

        decimal = casasCensadas / casas_total_censador
        porcentaje = str(int(decimal*100)) + "%"
        porcentajesCencistas[censador] = porcentaje

    return porcentajesCencistas
