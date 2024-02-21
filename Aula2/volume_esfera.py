# Calcular o volume e a area de uma esfera
# v = 4/3 pi.r³
import math
pi = math.pi

print('Vamos calcular o volume de uma esfera! :)')
try:
    r = float(input('Informe o raio da esfera: '))
except:
    print('Valor inválido!')

v = (4/3) * pi * (math.pow(r,3))
a = 4 * pi * (math.pow(r,2))

print('O volume da esfera é ', v, ' e sua área é ', a)