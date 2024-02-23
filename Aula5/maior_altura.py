# Entre 10 alturas aleatórias, encontrar a maior e a média
import random
soma = 0
maior = 0

for x in range(10):
    alt = random.uniform(1.5, 2.10) # numero aleatorio no intervalo
    print(f'Altura: {alt:.3f}')

    soma = soma + alt
    if alt > maior:
        maior = alt

media = soma / 10
print(f'Média das alturas: {media:.3f}')
print(f'Maior altura: {maior:.3f}')