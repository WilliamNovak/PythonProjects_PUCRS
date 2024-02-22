# Implemente um programa que lê um único valor inteiro de 4 dígitos e inverta o valor

try:
    n = int(input('Informe um inteiro de 4 dígitos: '))
except:
    print('Valor deve ser um inteiro!')

if len(str(n)) != 4:
    print('Número deve ter 4 dígitos!')
else:
    milhar = n//1000
    r = n%1000
    centena = r//100
    r = r%100
    dezena = r//10
    unidade = r%10

    print(n, 'invertido é', unidade*1000 + dezena*100 + centena*10 + milhar)