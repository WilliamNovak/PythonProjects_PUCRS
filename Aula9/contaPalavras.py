import string, nltk
nltk.download('stopwords')

# stopwords sao palavras como (de, e, ao, as, das, o) que nao queremos contar
stopwords = nltk.corpus.stopwords.words('portuguese') 

freq = {}

with open("dom_casmurro.txt", encoding="utf8") as arq:
    inicio = False
    # Para cada linha no texto:
    for linha in arq:
        linha = linha[:-1] # remove ultimo caracter (quebra de linha)

        if linha == 'I': # livro só começa na letra I, capitulo 1
            inicio = True
        if not inicio or linha == "": continue # Pula linhas anteriores ou em banco
        
        linha = linha.lower()

        for pont in string.punctuation: # remove pontuacao e caracteres especiais
            linha = linha.replace(pont,"")
        
        # palavras da linha
        for pal in linha.split(" "):
            if len(pal) < 3 or pal in stopwords: continue # desconsidera palavras pequenas ou stopwords
            
            if pal not in freq:
                freq[pal] = 0
            freq[pal] = freq[pal] + 1

cont = 1
# Primeiras 30 palavras, em ordem decrescente de frequência
for chave,valor in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{cont:3} - [{chave}] => {valor}")
    cont += 1
    if cont > 30:
        break