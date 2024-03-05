import random
roupas = []

for cont in range(50):
    tamanho = random.choice(['P','M','G'])
    cor = random.choice(['Branco','Preto','Azul'])
    roupas.append((tamanho, cor))

print(roupas)

qtdP = 0
qtdM = 0
qtdG = 0
qtdBranco = 0
qtdPreto  = 0
qtdAzul   = 0

for item in roupas:
    if   item[0] == 'P': qtdP += 1
    elif item[0] == 'M': qtdM += 1
    else: qtdG += 1
    
    if   item[1] == 'Branco': qtdBranco += 1
    elif item[1] == 'Preto': qtdPreto += 1
    else: qtdAzul += 1

maiorTamanho = 0

if qtdP >= qtdM and qtdP >= qtdG: 
    tamanhoMaisVendido = 'P'
    maiorTamanho = qtdP
elif qtdM >= qtdG: 
    tamanhoMaisVendido = 'M'
    maiorTamanho = qtdM
else: 
    tamanhoMaisVendido = 'G'
    maiorTamanho = qtdG

maiorCor = 0

if qtdBranco >= qtdPreto and qtdBranco >= qtdAzul: 
    corMaisVendida = 'Branco'
    maiorCor = qtdBranco
elif qtdPreto >= qtdAzul: 
    corMaisVendida = 'Preto'
    maiorCor = qtdPreto
else: 
    corMaisVendida = 'Azul'
    maiorCor = qtdAzul

print(f'Tamanho que mais vendeu: {tamanhoMaisVendido} - Peças: {maiorTamanho}')
print(f'Quantidade de peças de tamanho M vendidas: {qtdM}')
print(f'Cor preferida dos clientes: {corMaisVendida} - Peças: {maiorCor}')
