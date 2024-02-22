# Faça um programa que leia o horário de inicio de um jogo, em horas e minutos, e o horário de fim desse jogo, também em hora e minutos. 
# Sabendo que a duração máxima do jogo é de 24 horas, determine o tempo de duração do jogo em horas e minutos
try:
    h1 = int(input('Informe a hora de início do jogo: '))
    min1 = int(input('Informe os minutos de início do jogo: '))
    h2 = int(input('Informe a hora de fim do jogo: '))
    min2 = int(input('Informe os minutos de fim do jogo: '))
except:
    print('Valor inválido!')

m1 = h1 * 60 + min1
m2 = h2 * 60 + min2

if m1 < m2: d = m2 - m1
else: d = 24*60 - m1 + m2

print('O jogo durou',d//60,'horas e',d%60,'minutos.')