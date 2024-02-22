# Jogo de pedra, papel, tesoura contra o computador
import random

print('Vamos jogar pedra, papel e tesoura!')
try:
    user = int(input('Escolha 1 - Pedra, 2 - Papel, 3 - Tesoura: '))
except:
    print('Valor inválido!')

if user < 1 or user > 3:
    print('Escolha 1, 2 ou 3.')
else:
    if user == 1: u = 'Pedra'
    elif user == 2: u = 'Papel'
    else: u = 'Tesoura'

    computer = random.randint(1,3) # sorteia um valor de 1 a 3
    if computer == 1: c = 'Pedra'
    elif computer == 2: c = 'Papel'
    else: c = 'Tesoura'

    print(u,'vs',c)

    if user == computer:
        print('Empate!')
    elif user == 1:
        if computer == 2:
            print('Você perdeu!')
        else:
            print('Você venceu!')
    elif user == 2:
        if computer == 3:
            print('Você perdeu!')
        else:
            print('Você venceu!')
    else:
        if computer == 1:
            print('Você perdeu!')
        else:
            print('Você venceu!')