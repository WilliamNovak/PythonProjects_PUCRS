# Codificação de um programa que calcule o fatorial de um valor natural
try:
    n = int(input('Informe um número natural: '))
except:
    print('Valor inválido!')

f = 1
aux = 2

if n < 0:
    print('Número não é natural.')
else:
    while aux <= n:
        f = f * aux
        aux += 1

print(f'Fatorial de {n} é {f}')