# Codificação de um programa que escreva os divisores de um número
try:
    n = int(input('Informe um número natural: '))
except:
    print('Valor inválido!')

aux = 1

if n < 0:
    print('Número não é natural.')
else:
    print(f'Divisores de {n}:')
    while aux <= n:
        if n%aux == 0:
            print(aux)
        aux += 1