# Exemplos com dicionarios
dic = {}
dic["Fulano"] = "99817-9123"
dic["Beltrano"] = "99671-7562"
dic["Ciclano"] = "99881-1642"

print(dic.keys()) # chavees do dicionario
print(dic.values()) # valores do dicionario
print(dic.items()) # chaves e valores
print(dic.get('Ciclano')) # alternativa que nao dá erro se nao existir

nome = ''
while nome != "fim":
    print(dic)
    nome = input("Nome a procurar (fim para encerrar): ")
    
    if nome != "fim":
        if nome in dic:
            print(f"Telefone: {dic[nome]} removido!")
            del dic[nome] # deleta do dicionario
        else:
            print("Nome não encontrado!")