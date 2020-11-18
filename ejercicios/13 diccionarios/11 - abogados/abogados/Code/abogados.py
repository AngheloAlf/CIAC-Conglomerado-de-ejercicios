def juicios_por_mes(abogados):
    juicios = {}

    for nombre in abogados:
        diccionario = abogados[nombre]

        # desempaquetamos directamente la tupla
        for mes,cantidad in diccionario['juicios']:
            if mes not in juicios:
                juicios[mes] = 0
            juicios[mes] += cantidad

    return juicios

def total_juicios(abogados, nombre):
    total = 0

    diccionario = abogados[nombre]
    for mes,cantidad in diccionario['juicios']:
        total += cantidad
    return total

def quien_trabajo(abogados, empresa):
    lista = []
    for nombre in abogados:
        diccionario = abogados[nombre]
        if empresa in diccionario['empresas']:
            lista.append(nombre)
    return lista

def se_conocen(abogados, abogado_1, abogado_2):
    empresas_1 = abogados[abogado_1]['empresas']
    empresas_2 = abogados[abogado_2]['empresas']
    for empresa in empresas_1:
        if empresa in empresas_2:
            return True
    return False
