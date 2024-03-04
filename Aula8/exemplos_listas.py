lista1 = [1, 3, 2, "bola", "abacaxi"]

for item in lista1:
    print(item)

print(f'Quantidade de itens na lista: {len(lista1)}')

indice = 0
while indice < len(lista1):
    print(lista1[indice])
    indice += 1

lista2 = lista1 + [4, "gato", 9]
print(lista2)

lista3 = lista1 * 3
print(lista3)

if 'bola' in lista1: print('bola esta na lista')

lista2.append('cachorro')
lista2.append([2, 'leao', 6])
print(lista2)

lista4 = []
lista4.insert(0, 'python')
lista4.insert(0, 'o')
print(lista4)

print(lista2)
lista2.pop()
print(lista2)
lista2.pop(2)
print(lista2)
lista2.remove('gato')
print(lista2)