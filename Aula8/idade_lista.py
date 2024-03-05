import random
idades = []

for cont in range(20):
    idades.append(random.randint(1,81))

media = sum(idades)/20
maior = max(idades)
menor = min(idades)

print(idades)
print(f'Média de idades: {media}')
print(f'Maior idade: {maior}')
print(f'Menor idade: {menor}')