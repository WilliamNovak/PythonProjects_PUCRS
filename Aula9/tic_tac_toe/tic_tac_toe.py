# Implementar o Jogo da Velha em Python
import random

# Gera uma matriz com os valores do tabuleiro
def geraTabuleiro():
    tabuleiro = []
    for coluna in range(0,3):
        linha = []
        for l in range(0,3):
            linha.append(' ')
        tabuleiro.append(linha)
    return tabuleiro

# Percorre os dados da matriz e desenha o jogo da velha com os dados
def desenhaTabuleiro(tabuleiro):
    print('\n----------------- Jogo da Velha -----------------')
    print()
    indices = [0, 1, 2]
    print('\t\t0\t1\t2')
    print()
    for i in indices:
        print('\t', i, '\t', end='') # \t = tab e end='' nao quebra linha
        for j in indices:
            if j != 2: print(tabuleiro[i][j], '  |   ', end='')
            else: print(tabuleiro[i][j], end='')
        print()
        if i != 2: print('\t     -----------------------')
    print('\n-------------------------------------------------')

# Funcao para validar linhas e colunas informadas
def valida(valor):
    if valor >= 0 and valor <= 2:
        return True
    return False

# Jogada do usuario - Informa, valida e preenche posicao no jogo
def jogaUsuario(tabuleiro):
    print()
    try: linha = int(input('\tInforme a linha: '))
    except: linha = -1 
    try: coluna = int(input('\tInforme a coluna: '))
    except: coluna = -1 

    # Repete ate usuario informar uma linha e coluna nao ocupadas e validas
    while not(valida(linha)) or not(valida(coluna)) or not (tabuleiro[linha][coluna]==' '):
        print('\tIndices fora do intervalo válido ou célula ocupada.')
        try: linha = int(input('\tInforme a linha: '))
        except: linha = -1 
        try: coluna = int(input('\tInforme a coluna: '))
        except: coluna = -1 
    
    tabuleiro[linha][coluna] = 'X'

# Sorteia jogada do computador
def jogaComputador(tabuleiro):
    # Sortei posicao do computador ate achar disponivel
    linha = random.randint(0,2)
    coluna = random.randint(0,2)
    while tabuleiro[linha][coluna] != ' ':
        linha = random.randint(0,2)
        coluna = random.randint(0,2)
    
    tabuleiro[linha][coluna]="O"

# Funcao para verificar se alguem venceu em linha
def verificaVencedorLinha(tabuleiro, caracter):
    for linha in tabuleiro:
        cont = 0
        for item in linha:
            if item == caracter: cont += 1
            else: 
                cont = 0
                break
        if cont==3: return True
    return False

# Funcao para verificar se alguem venceu em coluna
def verificaVencedorColuna(tabuleiro, caracter):
    col = 0
    while col <= 2:
        lin = 0
        cont = 0
        while lin <= 2:
            if tabuleiro[lin][col] == caracter: cont += 1
            else: 
                cont = 0
                break
            lin = lin + 1
        if cont==3: return True
        col = col + 1
    return False

# Funcao para verificar se alguem venceu na diagonal
def verificaVencedorDiagonal(tabuleiro, caracter):
    # Verifica primeira diagonal
    cont = 0
    for i in range(0,3):
        if tabuleiro [i][i] == caracter: cont += 1
        else: break
    if cont==3: return True

    # Verifica segunda diagonal
    cont = 0
    for i in range(0,3):
        if tabuleiro[i][2-i] == caracter: cont += 1
        else: break
    if cont==3: return True

    return False

# Verifica se houve algum vencedor
def verificaVencedor(tabuleiro, caracter):
    resultado = verificaVencedorLinha(tabuleiro,caracter)
    if resultado == True and caracter == 'X': return 1
    if resultado == True and caracter == 'O': return 2
    resultado = verificaVencedorColuna(tabuleiro,caracter)
    if resultado == True and caracter == 'X': return 1
    if resultado == True and caracter == 'O': return 2
    resultado = verificaVencedorDiagonal(tabuleiro,caracter)
    if resultado == True and caracter == 'X': return 1
    if resultado == True and caracter == 'O': return 2
    return 0

# Controla o jogo da velha
def jogoDaVelha():
    # Gera e mostra tabuleiro
    tab = geraTabuleiro()
    desenhaTabuleiro(tab)
    # Usuario faz primeira jogada
    jogaUsuario(tab)

    cont = 1
    vencedor = 0
    # Computador e usuario alternam 4 jogadas cada
    while cont<=4:
        # Computador joga e verifica se venceu
        jogaComputador(tab)
        vencedor = verificaVencedor(tab, 'O')
        if vencedor != 0: break

        desenhaTabuleiro(tab)
        
        # Usuario joga e verifica se venceu
        jogaUsuario(tab)
        vencedor = verificaVencedor(tab, 'X')
        if vencedor != 0: break

        cont = cont + 1

    desenhaTabuleiro(tab)
    
    if vencedor == 0: print("\tDeu velha!")
    else: 
      if vencedor == 2 : print("\tO computador venceu.")
      else:
        print("\tParabéns, você venceu!")
    return vencedor

# Grava vencedor no arquivo
def gravaVencedor(nome, arquivo):
    arq = open(arquivo, 'a')
    arq.write(nome + '\n')
    arq.close

# Le os vencedores do arquivo em uma lista
def leVencedores(arquivo):
    try:
        arq = open(arquivo,"r")
    except FileNotFoundError: # Caso nao exista o arquivo
        return []
    vencedores = []
    for linha in arq:
        vencedores.append(linha[:-1])
    return vencedores

# Escreve a lista dos vencedores
def escreveLista(lista):
    print("\nVencedores:")
    if lista==[]: print("Nao há vencedores ainda")
    for item in lista:
        print(item)

# Reproduz programa
while True:
    print(" \n---- M E N U ---- ")
    print("1 - Jogar ")
    print("2 - Ver vencedores")
    print("0 - Sair")

    try:
        op = int(input("\nInforme a opção: "))

        if op == 0: 
            print("Fim do programa")
            break
        else:
            if op == 1: 
                vencedor = jogoDaVelha()
                if vencedor == 0: 
                    gravaVencedor("empate", "tic_tac_toe.txt")
                else:
                    if vencedor == 1:
                        nome = input("\tInforme o seu nome: ")
                        gravaVencedor(nome, "tic_tac_toe.txt")
                    else:
                        gravaVencedor("computador", "tic_tac_toe.txt")
            else:
                if op==2: 
                    dados = leVencedores("tic_tac_toe.txt")
                    escreveLista(dados)
                else: print("Opção inválida!")
    except:
        print("Opção inválida!")