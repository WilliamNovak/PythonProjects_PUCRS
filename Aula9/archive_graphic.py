import matplotlib.pyplot as plt

def carregaDados(nomeArq):
    aux = []
    with open(nomeArq) as csv: # Abre arquivo
        csv.readline() # Pula primeira linha (cabecalho)
        for linha in csv:
            nova = [float(val) for val in linha.split(',')] # Pega valores da primeira linha
            aux.append(nova) # Adiciona valores na lista
    return aux

dados = carregaDados('california_housing_test.csv')

longitudes = [aux[0] for aux in dados]
latitudes = [aux[1] for aux in dados]

plt.plot(longitudes, latitudes, 'bo')
#plt.scatter(longitudes, latitudes, s=1)
plt.show()

# Mapa com o Exemplo Acima
import folium

# Cria um mapa com as coordenadas e zoom
map = folium.Map(location=[36.7783,-119.4179], zoom_start=6, min_zoom=5)

for aux in dados:
    # Para cada ponto, cria um marcador e adiciona no mapa
    folium.CircleMarker(radius=1, location=[aux[1],aux[0]]).add_to(map)

map # Mostra o mapa