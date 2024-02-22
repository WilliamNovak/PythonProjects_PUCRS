# Implemente um programa que leia três valores e escreva o maior deles
try:
    num1 = int(input('Informe um número inteiro:'))
    num2 = int(input('Informe outro número inteiro:'))
    num3 = int(input('Informe outro número inteiro:'))
except:
    print('Número deve ser um inteiro!') 

if num1 >= num2 and num1 >= num3:
    print('O maior número é',num1)
elif num2 >= num1 and num2 >= num3:
    print('O maior número é',num2)
else:
    print('O maior número é',num3)