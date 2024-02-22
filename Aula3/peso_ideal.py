# Faça um programa que leia a altura de uma pessoa em metros e o gênero (use 1 para feminino e 2 para masculino). 
# A seguir, o programa deve escrever o peso ideal dessa pessoa, conforme descrito a seguir:
# Para homens, o peso ideal corresponde a 72.7 × altura − 58;
# Para mulheres, use 62.1 × altura − 44.7
try:
    a = float(input('Digite sua altura em metros:'))
except:
    print('Altura inválida!')

if a <= 0:
    print('Altura inválida!')
else:
    try:
        g = int(input('Informe seu gênero (1 - Feminino, 2 - Masculino):'))
    except:
        print('Gênero inválido!')
    
    if g == 1:
        p = 62.1 * a - 44.7
        print('Seu peso ideal é:',p)
    elif g == 2:
        p = 72.7 * a - 58
        print('Seu peso ideal é:',p)
    else:
        print('Gênero inválido!')