def calcula(base, duracao = 12):
    global taxa # acessa a variavel global no escopo local para poder alterar valor (nao recomendado)
    taxa = taxa + 0.1
    final = base * (1+taxa) ** duracao
    return final

b = float(input('Valor inicial: '))
taxa = float(input('Taxa de juros mensal: ')) #variavel global
#d = int(input('Duração (meses): '))

res = calcula(b)
print(f'Valor do final do período: {res:.2f}')
print(f'Valor da taxa de juros: {taxa}')