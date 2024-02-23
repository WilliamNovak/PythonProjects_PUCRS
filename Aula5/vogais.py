# Contar vogais em uma string
texto = input('Digite uma uma string: ')
vogais = 'aeiouAEIOU'
totalVogais = 0

for letra in texto:
    if letra in vogais:
        totalVogais += 1

print(f'A string tem {totalVogais} vogais.')