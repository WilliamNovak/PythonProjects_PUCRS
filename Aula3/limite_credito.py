# Implemente um programa que leia o saldo médio de uma conta, calcule e escreve o limite conforme a tabela abaixo:
# saldo médio                  - limite
# menor que R$ 500,00          - não há limite
# de R$ 500,00 a R$ 1.000,00   - 8% do saldo médio
# maior ou igual a R$ 1.000,00 - 15% do saldo médio
try:
    s = float(input('Informe o saldo médio da conta: '))
except:
    print('Valor inválido!')

if s < 500: print('Não há limite!')
elif s >= 500 and s < 1000: print('Limite:',s*0.08)
else: print('Limite:',s*0.15)