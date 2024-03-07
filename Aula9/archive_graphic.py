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

# Mapa com clustering (agrupamento) usando plugin
from folium.plugins import MarkerCluster

map2 = folium.Map(location=[36.7783,-119.4179], zoom_start=6, min_zoom=5)

marker_cluster = MarkerCluster().add_to(map2)

for aux in dados:
    folium.CircleMarker(radius=1, location=[aux[1],aux[0]]).add_to(marker_cluster)

map2 # Mostra o mapa

# Mapa de calor (HeatMap)
from folium.plugins import HeatMap

map3 = folium.Map(location=[36.7783,-119.4179], zoom_start=6, min_zoom=5)

aux2 = [[aux[1],aux[0],aux[7]] for aux in dados]

HeatMap(aux2, min_opacity=0.1).add_to(map3) # Mostra o mapa