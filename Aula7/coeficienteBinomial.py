# Calcular possibilidades de combinacoes (coeficiente binomial)
def fatorial(num):
    fat = 1
    for cont in range(1,num+1):
        fat = fat * cont
    return fat

def binomial(n,k):
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

def binomial2(n,k): # forma mais eficiente
    prod = 1
    total = k
    if n-k < k:
        total = n-k
    for i in range(1,total+1):
        prod = prod * ((n+1-i)/i)
    return int(prod)

print(binomial(4,2))
print(binomial(20,10))
print(binomial2(4,2))
print(binomial2(20,10))