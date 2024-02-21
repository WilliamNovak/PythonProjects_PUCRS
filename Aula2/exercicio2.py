# Faça um programa que converte de Fahrenheit para graus Celsius.
# Para realizar a conversão use a fórmula c = 5/9 (f-32)

try:
    f = float(input('Informe uma temperatura em Fahrenheit: '))
except:
    print('Temperatura deve ser numérico!')

c = 5/9 * (f - 32)

print(f, 'graus Fahrenheit equivalem a', c, 'graus Celsius.')