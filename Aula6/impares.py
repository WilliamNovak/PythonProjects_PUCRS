# Implemente um programa que leia dois valores, escreva e some os valores ímpares existentes entre eles. 
try:
    n1 = int(input('Informe um valor natural: '))
    n2 = int(input('Informe outro valor natural: '))
except:
    print('Valor inválido!')

if n1 < 0 or n2 < 0: print('Valores devem ser naturais.')
else:
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    
    cont = menor + 1
    soma = 0
    
    print(f'Ímpares entre {menor} e {maior}:')
    while cont < maior:
        if cont%2 != 0:
            print(cont)
            soma += cont
        cont += 1
    
    print(f'Soma dos números ímpares: {soma}')