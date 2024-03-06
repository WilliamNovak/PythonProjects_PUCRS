import matplotlib.pyplot as plt

# Exemplo 1 - Grafico
plt.plot([1,2,3,4],[2,4,9,16]) # Define coordenadas X e Y
plt.show() # Gera o grafico

# Exemplo 2 - Grafico com listas e repeticao
listaX = [x for x in range(10)]
listaY = [x**2 for x in range(10)]

plt.plot(listaX, listaY) # Define coordenadas conforme listas
plt.show()

plt.plot(listaX, listaY, 'ro') # Estilo para linha (r = cor, o = formato) - Padrao b-
plt.show()

# Exemplo 3 - Multiplas linhas
listaY2 = [x**3 for x in range(10)]
plt.plot(listaX, listaY,'r-')
plt.plot(listaX, listaY2,'bo')
plt.show()

# Exemplo 4 - Titulo Grafico
plt.plot(listaX, listaY,  'r-', label='$x^2$') # Define label para a linha
plt.plot(listaX, listaY2, 'bo', label='$x^3$') # Define label para a linha
plt.title('$x^2$ e $x^3$') # Define titulo do grafico
plt.legend() # Mostra legenda com os labels
plt.show()