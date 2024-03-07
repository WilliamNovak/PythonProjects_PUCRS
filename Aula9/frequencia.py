frase = input('Digite uma frase: ')
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