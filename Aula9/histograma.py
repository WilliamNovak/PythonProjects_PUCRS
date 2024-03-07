import matplotlib.pyplot as plt
import random

random.seed(42)
valores = [random.randint(0,11) for v in range(0,100)]
x = [v+0.5 for v in range(0,11)] # 0.5 centraliza valores de X no meio da barra

plt.hist(valores,x) # Define X e Y
plt.show()