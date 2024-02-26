# Escreva um programa que leia uma quantidade desconhecida de números. 
# Além disso, o programa deve contar e escrever a quantidade de valores pertencentes aos seguintes intervalos: [0;25], [26;50], [51;75] e [76;100].
# A entrada de dados deve terminar quando for lido um número negativo.
# Ao final da execução, o programa deve exibir ainda a quantidade de valores lidos.
n = 0
cont = 0
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while n >= 0:
    try:
        n = int(input('Informe um número inteiro: '))
    except:
        print('Valor inválido!')
    
    if n >= 0 and n < 26:
        intervalo1 += 1
    elif n > 25 and n < 51:
        intervalo2 += 1
    elif n > 50 and n < 76:
        intervalo3 += 1
    elif n > 75 and n < 101:
        intervalo4 += 1
    
    cont += 1

print(f'{cont} números informados.')
print(f'{intervalo1} números no intervalo de 0 a 25.')
print(f'{intervalo2} números no intervalo de 26 a 50.')
print(f'{intervalo3} números no intervalo de 51 a 75.')
print(f'{intervalo4} números no intervalo de 76 a 100.')