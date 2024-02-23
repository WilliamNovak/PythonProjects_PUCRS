# Digite um nome e retorne as iniciais do nome e sobrenome(s)
nome = input('Informe seu nome: ')
inicio = True

for letra in nome:
    if inicio:
        print(f'{letra}. ', end='')
        inicio = False
    
    if letra == ' ':
        inicio = True