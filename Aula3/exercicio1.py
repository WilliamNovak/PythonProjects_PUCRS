#Codifique um programa que leia um valor inteiro e indique se o valor é positivo, negativo ou zero
try:
    num = int(input('Informe um número inteiro:'))
except:
    print('Número deve ser um inteiro!')

if num > 0:
    print('Positivo!')
elif num < 0:
    print('Negativo!')
else:
    print('Zero!')