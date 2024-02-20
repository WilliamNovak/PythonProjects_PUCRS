# Calcular o volume de uma esfere
# v = 4/3 pi.r³
pi = 3.14

print('Vamos calcular o volume de uma esfera! :)')
print('Informe o raio da esfera: ')
try:
    r = int(input())
except:
    print('Valor inválido!')

v = (3/4) * pi * (r**3)

print('O volume da esfera é ', v)