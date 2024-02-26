somaIdade = 0
cont = 0
somaAltura = 0
meninas = 0
mais20 = 0
maiorIdade = 0
maiorAltura = 0

while cont<10:
  print("Cont: ", cont)
  idade = int(input("Informe a idade do estudante: "))
  while idade <= 0 or idade >= 120:
    print("> Idade invalida. Deve estar no intervalo (0;120). ")
    idade = int(input("> Informe novamente a idade do estudante: "))
  
  altura = float(input("Informe a altura do estudante: "))
  while altura <= 0 or altura > 2.5:
    print("> Altura invalida. Deve estar no intervalo (0; 2,5)")
    altura = float(input("> Informe novamente a altura do estudante: "))
  
  genero = int(input("Informe o genero do estudante usando 1 para feminino e 2 para masculino"))
  while genero != 1 and genero != 2:
    print("> Genero invalido. Deve ser 1 ou 2")
    genero = int(input("> Informe novamente o genero do estudante usando 1 para feminino e 2 para masculino"))

  somaIdade = somaIdade + idade
  cont = cont + 1

  if genero == 1:
    somaAltura = somaAltura + altura
    meninas = meninas + 1
  
  if idade>20: mais20 = mais20+1

  if idade>maiorIdade:
    maiorIdade = idade
    maiorAltura = altura

print("==========================================================================")
print("Media de idade dos estudantes: ", somaIdade/cont)
if meninas == 0: print("Nao foram informados dados de meninas")
else: print("Media de altura das meninas: ", somaAltura/meninas)
print("Percentual de alunos com mais de 20 anos: ", mais20*100/cont)
print("Altura do mais velho: ", maiorAltura, " Idade do mais velho: ", maiorIdade)