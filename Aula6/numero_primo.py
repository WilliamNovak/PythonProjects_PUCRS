# Implemente um programa que leia um valor inteiro e que verifica se o valor lido é primo
try:
    n = int(input('Informe um número natural: '))
except:
    print('Valor inválido!')

aux = 2
primo = True

if n < 0:
    print('Número não é natural.')
else:
    while aux < n:
        if n%aux == 0:
            primo = False
            break
        aux += 1

if primo: print(f'{n} é primo.')
else: print(f'{n} não é primo.')