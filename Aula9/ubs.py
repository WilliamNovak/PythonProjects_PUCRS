import folium
from folium.plugins import MarkerCluster

map = folium.Map(location=[-30,-51], zoom_start=6, min_zoom=5)
marker_cluster = MarkerCluster().add_to(map)

unidades = {}

with open("UBS.csv") as csv:
    print(csv.readline()) # mostra cabeçalho
    
    for linha in csv:
        aux = linha[:-1].split(';') # Dados da linha
        lat = aux[6]
        lon = aux[7]
        uf = aux[1]
        if lat != '' and lon != '' and uf == "43": # filtrando apenas RS
            nome = aux[3][1:-1]
            logr = aux[4][1:-1]
            bairro = aux[5][1:-1]
            lat = float(lat.replace(',','.'))
            lon = float(lon.replace(',','.'))
            unidades[nome] = (logr,bairro,lat,lon) # adiciona unidade
            folium.Marker(popup=nome, location=[lat,lon]).add_to(marker_cluster)

map

ubs = input("Nome da UBS: ").upper()

# Consulta direta por chave (dicionário)
if ubs in unidades:
    print(unidades[ubs])
else:
    print("Não encontrada")

# Consulta parcial por chave (sequencial)
for nome in unidades.keys():
    if ubs in nome:
        print("Parcial: ",nome,unidades[nome])