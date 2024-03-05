frases = ['Eu estudo Análise e Desenvolvimento de Sistemas na PUCRS',
          'Python é uma linguagem de programação muito bacana',
          'Exercício para aprender sobre tokenização de listas dentro de listas']

tokens = []
for frase in frases:
    print(frase)
    tokens.append(frase.split())

for frase in tokens:
    print('Palavras da frase:', frase)
    for palavra in frase:
        print(palavra)