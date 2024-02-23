# Verificar se uma senha é forte
# Mínimo 8 dígitos
# Pelo menos uma letra maiúscula
# Pelo menos um dígito
# Pelo menos um caracter de pontuação
import string
senha = input('Digite uma senha: ')

maiuscula = False
digito = False
pontuacao = False

if len(senha) < 8:
    print('Senha é muita curta')
else:
    for letra in senha:
        if letra in string.ascii_uppercase:
            maiuscula = True
        if letra in string.digits:
            digito = True
        if letra in string.punctuation:
            pontuacao = True
    
    if maiuscula == False: print('Senha não tem maiúsculas')
    elif digito == False: print('Senha não tem dígitos')
    elif pontuacao == False: print('Senha não tem caractere de pontuação')
    else: print('Senha forte')