import random
lista = []

for cont in range(30):
    lista.append(random.randint(1,100))

print(f'Lista original: {lista}')

lista.sort()
lista.reverse()

maiores = []
indice = 0
while indice < 10:
    maiores.append(lista[indice])
    indice += 1

print(f'Lista dos 10 maiores: {maiores}')