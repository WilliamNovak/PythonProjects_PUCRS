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
        aux = {'nome': dados[1], 'votos': 0, 'vagas': 0, 'media': 0}
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

print(f'Total de votos: {totalVotos}')

# 4.1 Calcular o quociente eleitoral geral (validos/vagas)
qe = totalVotos//vagas
print(f'QE: {qe}')

# 4.2 e partidário (qp = votos partido / qe)
# 5. Com base nesses cálculos, determinar quantas vagas cada partido receberá inicialmente (vagas = qp)
vagasDistribuidas = 0

for sigla, dados in partidos.items():
    qp = dados['votos'] // qe
    if qp > 0:
        dados['vagas'] = qp
        vagasDistribuidas += qp
        print(sigla,dados)

# print(f'Total de vagas distribuídas: {vagasDistribuidas}')

# 6. Considerando as vagas que restam, atribui-las a cada partido, de acordo com o cálculo da média (número de votos válidos recebido pelo partido dividido pelo total de vagas já recebidas + 1).

# Calcula da media dos partidos
for sigla, dados in partidos.items():
    md = dados['votos'] // (dados['vagas'] + 1)
    dados['media'] = md

# Percorre os partidos por ordem decrescente de media atribuindo vagas restantes
for sigla,dados in sorted(partidos.items(), key=lambda x: x[1]['media'], reverse=True):
    if vagasDistribuidas < vagas:
        vagasDistribuidas += 1
        dados['vagas']    += 1

# Guarda as vagas dos partidos
salvaVagas = {}
for p in partidos:
    salvaVagas[p] = partidos[p]['vagas']

# 7. Determinar os(as) candidatos(as) eleitos(as), apresentando uma tabela com o nome, total de votos recebidos e nome completo do partido. É necessário percorrer todos os candidatos, em ordem decrescente de votos - enquanto houver vagas para o partido, indica que o candidato foi eleito.
for nome, dados in sorted(candidatos.items(), key=lambda x:x[1]['votos'], reverse=True):
    sigla = dados['sigla']
    if partidos[sigla]['vagas'] > 0:
        partidos[sigla]['vagas'] -= 1
        print(f'{nome:40} {sigla:4} {dados["votos"]} votos')

# 8. Desenhar, em um gráfico de barras, a distribuição de vagas na Câmara para cada partido (partidos sem vagas não devem sem exibidos). Pode ser em ordem de vagas, ou não.
import matplotlib.pyplot as plt

nomes = []
valores = []

for p in salvaVagas:
    if salvaVagas[p] > 0:
        nomes.append(p)
        valores.append(salvaVagas[p])

plt.figure(figsize=(10,4))
plt.xticks(rotation=30, ha='right')
plt.bar(nomes,valores)
plt.show()