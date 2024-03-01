# Calcular possibilidades de combinacoes (coeficiente binomial)
def fatorial(num):
    fat = 1
    for cont in range(1,num+1):
        fat = fat * cont
    return fat

def binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

print(binomial(4,2))
print(binomial(20,10))