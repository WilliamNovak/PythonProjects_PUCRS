# Calculo do somatorio de todos uns números até um determinado (acumulador)
try:
    num = int(input('Informe um número inteiro: '))
except:
    print('Valor inválido!')

soma = 0
for x in range(1,num+1):
    soma = soma + x

print(f'Somatório dos números de 1 até {num}: {soma}')