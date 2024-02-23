# Verificar se uma string invertida é igual (palíndromo)
texto = str(input('Digite uma uma string: '))

if texto == texto[::-1]:
    print(f'{texto} é um palíndromo!')
else:
    print(f'{texto} não é um palíndromo!')