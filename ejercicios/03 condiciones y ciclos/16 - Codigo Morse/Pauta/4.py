# Codigo Morse

def transformar(numero):
    if numero<6:
        return numero*'o'+(5-numero)*'-'
    else:
        return (numero-5)*'-'+(10-numero)*'o'