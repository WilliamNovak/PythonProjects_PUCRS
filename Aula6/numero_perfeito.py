# Implementação de um programa que leia um valor e verifique se ele é perfeito (para sê-lo, ele deve corresponder à soma dos seus divisores próprios)
try:
    n = int(input('Informe um número inteiro e positivo: '))
except:
    print('Valor inválido!')

if n <= 0:
    print('Número deve ser maior que 0.')
else:
    aux = 2
    soma = 1

    while aux < n:
        if n%aux == 0:
            soma += aux
        aux += 1
    
    if n == soma: print(f'{n} é perfeito.')
    else: print(f'{n} não é perfeito.')