# Construa um programa que lê o tempo de um evento em segundos e o escreve decomposto em horas, minutos e segundos
import math

try:
    s = int(input('Digite o tempo do evento em segundos: '))
except:
    print('Valor deve ser um inteiro!')

min = math.trunc(s / 60)
s = s % 60

h = math.trunc(min / 60)
min = min % 60

print('O evento dura ',h,'horas,',min,'minutos e',s,'segundos.')