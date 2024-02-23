# Foram entrevistados 2000 habitantes de uma cidade. De cada habitante foram coletados os seguintes dados: idade, renda, gênero e número de filhos
# a) Média de renda;
# b) Média de idade de quem tem mais de 3 filhos;
# c) Quantidade de homens com menos de 30 anos;
# d) Média do número de filhos;
# e) Renda do homem mais velho;
# f) Idade da mulher com maior renda.
import random
somaRenda = 0
somaIdade = 0
qtdTresFilhos = 0
qtdHomens = 0
somaNumeroFilhos = 0
idadeHomemMaisVelho = 0
rendaHomemMaisVelho = 0
rendaMulherMaiorRenda = 0
idadeMulherMaiorRenda = 0

totalHab = 2000
for hab in range(totalHab):
    idade = random.randint(18,80)
    renda = random.uniform(1100,12000)
    genero = random.choice(['H','M'])
    filhos = random.randint(0,5)

    somaRenda += renda
    somaNumeroFilhos += filhos
    
    if filhos > 3:
        somaIdade += idade
        qtdTresFilhos += 1
    
    if genero == 'H':
        if idade < 30:
            qtdHomens += 1

        if idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            rendaHomemMaisVelho = renda
    else:
        if renda > rendaMulherMaiorRenda:
            rendaMulherMaiorRenda = renda
            idadeMulherMaiorRenda = idade
    
mediaRenda = somaRenda / totalHab
mediaIdade = somaIdade // qtdTresFilhos
mediaFilhos = somaNumeroFilhos // totalHab

print(f'A média de renda é R${mediaRenda:.2f}')
print(f'A média de idade de quem tem mais de 3 filhos é {mediaIdade}')
print(f'A quantidade de homens com menos de 30 anos é {qtdHomens}')
print(f'A média do número de filhos é {mediaFilhos}')
print(f'A renda do homem mais velho é R${rendaHomemMaisVelho:.2f}')
print(f'A idade da mulher com maior renda é {idadeMulherMaiorRenda}')