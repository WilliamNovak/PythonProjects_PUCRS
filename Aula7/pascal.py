# Triangulo de Pascal

def binomial2(n,k): # forma mais eficiente
    prod = 1
    total = k
    if n-k < k:
        total = n-k
    for i in range(1,total+1):
        prod = prod * ((n+1-i)/i)
    return int(prod)

def pascal(linhas):
    for linha in range(linhas):
        for coluna in range(linha+1):
            valor = binomial2(linha,coluna)
            print(f'{valor} ', end='')
        print()
    
pascal(10)