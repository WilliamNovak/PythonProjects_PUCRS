# Foram entrevistados 50 alunos
# Foram coletados os seguintes dados: idade, semestre e curso
# Ler (sortear) os dados e escrever: a media de idade, o curso do aluno mais velho e a quantidade de alunos no quinto semestre
import random
somaIdade = 0
maiorIdade = 0
cursoMaisVelho = ''
qtdQuinto = 0

for x in range(50):
    idade = random.randint(18, 60)
    curso = random.choice(['ADS', 'Eng. Software', 'Ciências da Computação', 'Sistemas da Informação'])
    semestre = random.randint(1,10)

    somaIdade += idade

    if idade > maiorIdade:
        maiorIdade = idade
        cursoMaisVelho = curso
    
    if semestre == 5:
        qtdQuinto += 1

mediaIdade = somaIdade // 50
print(f'Média das idades: {mediaIdade}')
print(f'Curso do aluno mais velho: {cursoMaisVelho}')
print(f'Quantidade de alunos no quinto semestre: {qtdQuinto}')