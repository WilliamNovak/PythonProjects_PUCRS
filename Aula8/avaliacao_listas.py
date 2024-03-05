import random
notas = []
quantidade = []
conceito = []

for cont in range(25):
    notas.append(random.randint(1,6))

print(f'Notas: {notas}')

conceito.append('Excelente')
quantidade.append(notas.count(5))
conceito.append('Bom')
quantidade.append(notas.count(4))
conceito.append('Regular')
quantidade.append(notas.count(3))
conceito.append('Ruim')
quantidade.append(notas.count(2))
conceito.append('Péssimo')
quantidade.append(notas.count(1))

maiorQuantidade = quantidade[0]
maiorConceito = conceito[0]

for num in range(4):
    if quantidade[num] > maiorQuantidade:
        maiorQuantidade = quantidade[num]
        maiorConceito = conceito[num]
    
print(f'Conceito com mais votos: {maiorConceito}, Votos: {maiorQuantidade}')