# Implemente um programa que leie um valor n, calcule e escreva elevado a 2, 3 e 4
import math

try:
    n = int(input('Informe um número inteiro: '))
except:
    print('Valor inválido!')

print(n,'² = ',math.pow(n,2))
print(n,'³ = ',math.pow(n,3))
print(n,'^4 = ',math.pow(n,4))