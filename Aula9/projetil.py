import math, matplotlib.pyplot as plt

g = 9.81
ang = float(input("Ângulo:"))
v0 = float(input("Vel. inicial (m/s):"))
y0 = float(input("Altura inicial:"))
listax = []
listay = []
# Converte ângulo para radianos
ang = math.radians(ang)

y = 0
x = 0

while y >= 0:
    # Adiciona coordenadas
    listax.append(x)
    listay.append(y)
    
    # Calcula Y
    y = x * math.tan(ang) - (1/(2*v0*v0) 
        * g*x*x/math.cos(ang)**2) + y0
    x = x + 0.1

plt.xlabel("Distância")
plt.ylabel("Altura")
plt.plot(listax,listay,'bo')
plt.show()