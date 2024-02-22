# Elabore um programa que leia 3 notas, calcule e escreva a media ponderada considerando os pesos 5, 2.5 e 2.5.
# A maior nota deve ter peso 5.
try:
    n1 = float(input('Informe a nota 1: '))
    n2 = float(input('Informe a nota 2: '))
    n3 = float(input('Informe a nota 3: '))
except:
    print('Nota inválida!')

if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
    print('Notas devem estar no intervalo de 0 a 10.')
else:
    if n1 >= n2 and n1 >= n3: m = (n1 * 5 + n2 * 2.5 + n3 * 2.5)/10
    elif n2 >= n1 and n2 >= n3: m = (n2 * 5 + n1 * 2.5 + n3 * 2.5)/10
    else: m = (n3 * 5 + n1 * 2.5 + n2 * 2.5)/10
    print('Média ponderada:',m)