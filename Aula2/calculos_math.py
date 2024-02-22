# Construa um programa que leia dois valores inteiros e escreva na tela
# 1. a soma
# 2. a diferenca
# 3. a media
# 4. a distancia (valor absoluto da diferença)
# 5. o maior dos dois
# 6. o menor dos dois

import math

try:
    n1 = int(input('Informe o primeiro valor:'))
    n2 = int(input('Informe o primeiro valor:'))
except:
    print('Valor deve ser um inteiro!')

soma  = n1 + n2
dif   = n1 - n2
med   = soma/2
dist  = math.fabs(n1-n2)
maior = (n1 + n2 + math.fabs(n1 - n2))/2
menor = (n1 + n2 - math.fabs(n1 - n2))/2

print('A soma de',n1,'+',n2,'é igual a',soma)
print('A diferença de',n1,'-',n2,'é igual a',dif)
print('A média de',n1,'e',n2,'é igual a',med)
print('A distância de',n1,'e',n2,'é igual a',dist)
print('O maior número é',maior)
print('O menor número é',menor)