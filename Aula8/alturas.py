arquivo = open('alturas.txt','w')

for cont in range(5):
    nome = input('Informe o nome: ')
    altura = float(input('Informe a altura: '))
    arquivo.write(nome + ' - ' + str(altura) + '\n')

arquivo.close()

arq = open('alturas.txt', 'r')
lista = []
soma  = 0
maiorAltura = 0
nomeMaior = ''

for linha in arq:
    retorno = linha[:-1].split(' - ')
    altura = float(retorno[1])
    nome = retorno[0]
    dados = (nome, altura)

    soma += altura

    if altura > maiorAltura:
        maiorAltura = altura
        nomeMaior   = nome

    lista.append(dados)

arq.close()
print(lista)

media = soma / len(lista)

print(f'Média das alturas: {media:.2f}')
print(f'Nome da pessoa mais alta: {nomeMaior}')