dic = {}
dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"
dic["Pedro"] = "99123-2432"

for k in dic.keys():
    print(f"Chave: {k}")
print()

for v in dic.values():
    print(f"Valor: {v}")
print()

print("Chaves e valores em ordem de inclusão:")
for k,v in dic.items():
    print(f"{k:8} -> {v}")
print()

print("Ordenado pelas chaves:")
for k,v in sorted(dic.items()):
    print(f"{k:8} -> {v}")
print()

print("Ordenado pelos valores:")
for k,v in sorted(dic.items(),key=lambda x: x[1]):
    print(f"{k:8} -> {v}")