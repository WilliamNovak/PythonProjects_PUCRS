# Implemente um programa que leia um valor inteiro entre 1 e 7, correspondente ao dia da semana. 
# O programa deve escrever o dia da semana por extenso correspondente ao valor lido.
try:
    d = int(input('Informe o número do dia da semana: '))
except:
    print('Número inválido!')

if d == 1: print('Domingo!')
elif d == 2: print('Segunda!')
elif d == 3: print('Terça!')
elif d == 4: print('Quarta!')
elif d == 5: print('Quinta!')
elif d == 6: print('Sexta!')
elif d == 7: print('Sábado!')
else: print('Dia inválido!')