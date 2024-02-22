# Receba um ano e determine se ele é bissexto
# Deve ser divisível por 4
# Mas não por 100, a menos que seja divisível por 400
try:
    a = int(input('Informe um ano: '))
except:
    print('Valor inválido!')

if (a%400 == 0) or (a%4 == 0 and a%100 != 0):
    print(a,'é bissexto.')
else:
    print(a,'não é bissexto.')