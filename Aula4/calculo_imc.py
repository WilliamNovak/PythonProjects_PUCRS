# Receba o peso e altura de uma pessoa e calcule o IMC
try:
    a = float(input('Informe sua altura em metros: '))
    p = float(input('Informe seu peso e kg: '))
except:
    print('Valor inválido!')

if p < 0 or a < 0:
    print('Peso e altura devem ser maiores que 0.')

imc = p/a**2
print('Seu imc é',imc)

if imc < 18.6:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso normal')
elif imc < 35:
    print('Obesidade grau I')
elif imc < 40:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')