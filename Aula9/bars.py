import matplotlib.pyplot as plt
import random

random.seed(42) # Define semente para ser sempre a mesma
anos = [a for a in range(1990,2010)]
valores = [random.randint(100,1500) for v in range(len(anos))] # Gera um valor aleatorio para cada ano

plt.bar(anos,valores) # Define eixos X e Y do grafico
plt.xticks(range(1990,2010,2)) # Define divisao das barras - Mostrar anos, mas de 2 em 2
plt.show()