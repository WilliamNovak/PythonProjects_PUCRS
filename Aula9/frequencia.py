# Contar frequencia de letras em frase e quais foram usadas ou nao
import string

frase = input('Digite uma frase: ').lower()
dic = {}

for letra in frase:
    if letra == ' ': continue
    if letra in dic:
        dic[letra] += 1
    else:
        dic[letra] = 1

print('Frequência de caracteres na frase:')
for l,v in dic.items():
    print(f'{l} => {v}')

todasLetras = set(string.ascii_lowercase)
usadas      = set(dic.keys())
naoUsadas   = set(todasLetras - usadas)

print(f'Letras usadas    : {sorted(usadas)}')
print(f'Letras não usadas: {sorted(naoUsadas)}')