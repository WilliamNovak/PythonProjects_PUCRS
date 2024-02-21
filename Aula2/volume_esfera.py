# Calcular o volume de uma esfere
# v = 4/3 pi.r³
import math
pi = math.pi

print('Vamos calcular o volume de uma esfera! :)')
try:
    r = float(input('Informe o raio da esfera: '))
except:
    print('Valor inválido!')

v = (4/3) * pi * (math.pow(r,3))

print('O volume da esfera é ', v)