import random
lista = []

for cont in range(30):
    lista.append(random.randint(1,100))

print(f'Lista original: {lista}')

maiores = []
for cont in range(10):
    maiores.append(max(lista))
    lista.remove(max(lista))

print(f'Lista dos 10 maiores: {maiores}')