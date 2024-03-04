import random
maior = 0
qtdPares = 0

lista = []

for cont in range(30):
    lista.append(random.randint(1,500))

for item in lista:
    if item > maior:
        maior = item
    if item%2 == 0:
        qtdPares += 1

print(lista)
print(f'Maior: {maior}')
print(f'Quantidade de pares: {qtdPares}')