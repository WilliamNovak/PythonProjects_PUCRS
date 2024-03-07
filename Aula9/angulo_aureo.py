import matplotlib.pyplot as plt, cmcrameri.cm as cmc, math

listax = []
listay = []
dists = [] # distâncias ao centro

phi = (1 + math.sqrt(5))/2
angAureo = 360 - 360/phi

ang = 0

for cont in range(3000):
    dist = math.sqrt(cont) # distancia = raiz quadrada do contador
    ang = ang + angAureo # incrementa angulo com aureo
    ang_rad = math.radians(ang) # converte para radianos
    # Calcula coordenadas
    x = dist * math.cos(ang_rad)
    y = dist * math.sin(ang_rad)
    # Adiciona coordenadas e distancia
    listax.append(x)
    listay.append(y)
    dists.append(dist)

plt.figure(figsize=(8,8)) # Tamanho do grafico em polegadas

# Mapa de cor, de acordo com a distancia
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
plt.scatter(listax,listay,c=dists,cmap=cmc.bamako)
plt.show()