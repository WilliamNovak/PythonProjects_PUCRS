# Considerando a conjectura de Goldbach, o exemplo consiste na implementação de um programa que leia um valor n (inteiro e positivo) e escreva os n primeiros pares acima de 4, juntamente com os primos em que cada par pode ser decomposto.
try:
    n = int(input('Informe um a quatidade de números: '))
except:
    print('Valor inválido!')

if n < 1:
    print('Valor deve ser maior que 0.')
else:
    par = 6
    cont = 0

    print(f'Primeiros {n} pares acima de 4 decompostos em primos:')
    while cont < n:
        for x in range(1,par):

            primo = True
            aux = 2

            while aux < x:
                if x%aux == 0:
                    primo = False
                    break
                aux += 1
            
            if primo == True:
                for y in range(1,x):
                    primo = True
                    aux = 2

                    while aux < y:
                        if y%aux == 0:
                            primo = False
                            break
                        aux += 1
                    
                    if primo == True and y + x == par:
                        print(f'{par} = {x} + {y}')
                        break

        cont += 1
        par += 2
