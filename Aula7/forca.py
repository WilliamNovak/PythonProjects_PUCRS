import random
palavras = ["amarelo", "amiga", "amor", "ave", "bala", "bela", "bola", "bolo", "branco", "cama", "caneca", "celular", "clube", "computador", "copo", "doce", "elefante", "escola", "estojo", "faca", "foto", "garfo", "geleia", "girafa", "janela", "limonada", "meia", "noite", "ornitorrinco", "ovo", "pai", "parque", "passarinho", "peixe", "pijama", "rato", "rinoceronte", "umbigo", "zebra"]

def sorteio():
    return random.choice(palavras).upper()

def forca(vidas):
    if vidas == 0:
        print('''
               +---+
               |   |
               O   |
              /|\  |
              / \  |
                   |
              =========
              ''')
    elif vidas == 1:
        print('''
               +---+
               |   |
               O   |
              /|\  |
              /    |
                   |
              =========
              ''')
    elif vidas == 2:
        print('''
               +---+
               |   |
               O   |
              /|\  |
                   |
                   |
              =========
              ''')
    elif vidas == 3:
        print('''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
              =========
              ''')
    elif vidas == 4:
        print('''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
              =========
              ''')
    elif vidas == 5:
        print('''
               +---+
               |   |
               O   |
                   |
                   |
                   |
              =========
              ''')
    else:
        print('''
               +---+
               |   |
                   |
                   |
                   |
                   |
              =========
              ''')

# 1. Sorteia a palavra
palavra = sorteio()

# 2. Gera uma palavra com _
tam = len(palavra)
adivinhada = "_" * tam
vidas = 6
letras = ""

jogoAtivo = True

# 3. Enquanto o jogo estiver ativo:
while jogoAtivo:
  # 4. Exibe estado do jogo
  forca(vidas)
  print(adivinhada)
  print()
  print(f"Letras já escolhidas: {letras}")

  # 5. Aguarda a digitação de uma letra válida (ainda não escolhida)
  valida = False
  while not valida:
    letra = input("Escolha uma letra: ").upper()
    if letra not in letras:
      valida = True
    else:
      print("Esta letra já foi escolhida!")
  
  # Registra a letra digitada
  if letras == '': letras += letra
  else: letras += '-' + letra

  # 6. Verifica se a letra está na palavra:
  if letra in palavra:
    # - Se estiver, troca os _
    for pos in range(tam):
      if letra == palavra[pos]:
        adivinhada = adivinhada[:pos] + letra + adivinhada[pos+1:]
  else:
    # - Se não estiver, perde uma vida e verifica se o jogador perdeu
    print("Esta letra não está na palavra...")
    vidas -= 1
    if vidas == 0:
      forca(vidas)
      print("Infelizmente você perdeu...")
      jogoAtivo = False
  
  # 7. Verifica se o jogador ganhou
  if "_" not in adivinhada:
    print("Parabéns, você acertou!")
    jogoAtivo = False

# 8. Mostra a palavra sorteada
print(f"A palavra sorteada era {palavra}")