# Adivinhe um número sorteado pelo computador entre 1 e 100
# O jogador tem 10 chances para adivinhar
# A cada change informar se é menor, maior ou se acertou
import random
num = random.randint(1,100)

print('## Jogo da adivinhação ##')
print('-- Adivinhe o número entre 0 e 100 em 10 tentativas --')

for x in range (10):
    try:
        n = int(input('Qual o número? '))

        if n == num:
            print('Parabéns, você acertou!')
            break
        elif x == 9:
            print('Acabaram as tentativas :(')
            print(f'O número sorteado era: {num}')
        elif n < num:
            print(f'Errou! O número é maior que {n}')
        else:
            print(f'Errou! O número é menor que {n}')
    except:
        if x == 9:
            print('Acabaram as tentativas :(')
            print(f'O número sorteado era: {num}')
        else:
            print('Número inválido!')