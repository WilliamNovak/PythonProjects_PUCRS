# Divisores dos primeiros 100 números
numero = 1
while numero <= 100:
    aux = 1
    print(f'Divisores de {numero}:')
    while aux <= numero:
        if numero%aux == 0:
            print(aux)
        aux += 1
    numero += 1