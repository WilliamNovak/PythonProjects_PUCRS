# Implemente um programa que leia os valores a, b e c de uma formula de Bhaskara, calcule e escreva as raízes reais
import math

try:
    a = float(input('Informe o valor a: '))
    b = float(input('Informe o valor b: '))
    c = float(input('Informe o valor c: '))
except:
    print('Valor inválido!')

delta = math.pow(b,2) - 4 * a * c
if delta < 0 or a == 0: print('Erro, delta negativo ou divisão por zero.')
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)

print('x1:',x1)
print('x2:',x2)