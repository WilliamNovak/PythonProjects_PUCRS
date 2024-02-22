# Implemente um programa que determina o preço de venda dos produtos de uma loja conforme o preço de custo desses produtos. 
# O programa deve ler o preço de custo e calcular o valor de venda conforme a tabela abaixo:
# preço unitário de custo         - preço de venda
# valor abaixo de R$ 10,00        - lucro de 70%
# de R$ 10,00 a menos de R$ 30,00 - lucro de 50%
# de R$ 30,00 a menos de R$ 50,00 - lucro de 40%
# valor acima ou igual a R$ 50,00 - lucro de 30%
try:
    pc = float(input('Informe o preço de custo do produto: '))
except:
    print('Valor inválido!')

if pc < 10: pv = pc * 1.7
elif pc >= 10 and pc < 30: pv = pc * 1.5
elif pc >= 30 and pc < 50: pv = pc * 1.4
else: pv = pc * 1.3

print('Preço de venda do produto é de',pv,'reais.')