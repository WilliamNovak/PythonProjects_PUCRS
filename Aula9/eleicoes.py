# Exercicio - Determinar composição eleitoral de uma cidade
print('---------- COMPOSIÇÃO ELEITORAL MUNICIPAL ----------')

# 1. Ler os dados da votação e dos partidos, usando listas e/ou dicionários.

# 2. Perguntar ao usuário qual é a cidade desejada e o total de vagas na Câmara. Isso é necessário, pois a quantidade de vagas varia de acordo com o tamanho do município. Por exemplo, em Porto Alegre há 36 vagas, já em Caxias do Sul há 23, e em Viamão há 21. Você pode experimentar com outras cidades, basta saber o número exato.

# 3. Contabilizar os votos para cada partido, e para cada candidato(a) individual

cid   = input('Informe a cidade da eleição: ').upper()
vagas = int(input('Informe o número de vagas: '))

partidos = {}
candidatos = {}

totalVotos = 0

# Le os partidos, armazenando nome e votos
with open('partidos.csv', encoding='utf8') as arq:
    arq.readline()
    for linha in arq:
        dados = linha[:-1].split(',')
        # Busca e armazena informacoes do partido
        aux = {'nome': dados[1], 'votos': 0, 'vagas': 0 }
        partidos[dados[0]] = aux

# Le os candidados, armazenando nome e votos
with open('eleicoes-municipais.csv', encoding='utf8') as arq:
    arq.readline()
    for linha in arq:
        dados = linha[:-1].split(',')
        # Busca Informacoes do candidato
        cidade = dados[1]
        sigla  = dados[2]
        cargo  = dados[3]
        nome   = dados[4]
        votos  = int(dados[5])

        if cidade.upper() != cid or cargo != 'VEREADOR': continue
        
        if nome not in candidatos:
            candidatos[nome] = {'sigla': sigla, 'votos': 0}
        candidatos[nome]['votos'] += votos
        partidos[sigla]['votos'] += votos
        totalVotos += votos