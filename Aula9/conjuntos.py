# Exemplos com conjuntos

# cria conjunto vazio
conj = set() 
# adiciona elementos
conj.add(5)
conj.add(3)
conj.add(12)
print(conj)
# remove elemento
conj.remove(3)
print(conj)
# remove elemento aleatorio
conj.pop()
print(conj)
# limpa conjunto
conj.clear()
print(conj)

a = set([1,2,3,4,5,6])
b = set([4,5,6,7,8,9])
c = set([1,3,5])

print(f"união a+b: {a.union(b)}")
print(f"diferença a-b: {a.difference(b)}")
print(f"diferença b-a: {b.difference(a)}")
print(f"intersec. a&b: {a.intersection(b)}")
print(f"dif. sim. a^b: {a.symmetric_difference(b)}")
print(f"a contém c : {a.issuperset(c)}")
print(f"c contido a : {c.issubset(a)}")