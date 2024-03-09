def carregaDados(arquivo):
    arq = open(arquivo, 'r', encoding='utf8')
    dados = []
    for linha in arq:
        linha = linha[:-1]
        linha = linha[1:len(linha)] # remover virgula do inicio
        dados.append(linha)
    return dados

def converteLinha(linha):
    itens = linha.split(',')
    dadosLinha = [itens[0]]
    cont = 1
    while cont < len(itens):
        dadosLinha.append(float(itens[cont]))
        cont += 1
    return dadosLinha

def converteDados(dados):
    valores = []
    cont = 1
    while cont < len(dados):
        valores.append(converteLinha(dados[cont]))
        cont += 1
    return valores
    
def casosConfirmados(dados):
    confirmados = 0
    novosConfirmados = 0
    for linha in dados:
        confirmados += linha[1]
        novosConfirmados += linha[2]
    
    return (confirmados + novosConfirmados)

def obitosEstado(dados):
    obitos = 0
    novosObitos = 0
    for linha in dados:
        obitos += linha[4]
        novosObitos += linha[5]
    
    return (obitos + novosObitos)

def cidadeMaisNovosCasos(dados):
    novosCasos = dados[0][2]
    cidade = dados[0][0]
    for linha in dados:
        if linha[2] > novosCasos:
            novosCasos = linha[2]
            cidade = linha[0]
    return cidade

def cidadeMenorMortalidade(dados):
    menorMortalidade = dados[0][6]
    cidade = [0][0]
    for linha in dados:
        if linha[6] < menorMortalidade:
            menorMortalidade = linha[6]
            cidade = linha[0]
    return cidade

def mediaNovosObitos(dados):
    total = 0
    for linha in dados:
        total += linha[5]
    return (total / len(dados))

dados = carregaDados('SESRS - Coronavírus_v1.csv')
cabecalho = dados[0].split(',')
dadosConvertidos = converteDados(dados)

print(f'Total de casos confirmados (atuais e novos): {casosConfirmados(dadosConvertidos)}')
print(f'Total de óbitos no estado (atuais e novos): {obitosEstado(dadosConvertidos)}')
print(f'Cidade com mais novos casos: {cidadeMaisNovosCasos(dadosConvertidos)}')
print(f'Cidade com menor mortalidade do estado: {cidadeMenorMortalidade(dadosConvertidos)}')
print(f'Média de novos óbitos no estado: {mediaNovosObitos(dadosConvertidos):.2f}')
