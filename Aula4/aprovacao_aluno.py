# Aprovação do aluno por nota, frequência e exame
try:
    f = int(input('Informe a sua frequência nas aulas (em %): '))
except:
    print('Frequência inválida!')

if f < 0 or f > 100:
    print('Frequência deve estar entre 0 e 100%.')
elif f < 75:
    print('Reprovado por frequência.')
else:
    try:
        n1 = float(input('Informe a primeira nota: '))
        n2 = float(input('Informe a segunda nota: '))
        n3 = float(input('Informe a terceira nota: '))
    except:
        print('Nota inválida!')

    if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10 or n3 < 0 or n3 > 10:
        print('Notas devem estar no intervalo de 0 a 10.')
    else:
        g1 = (n1 + n2 + n3) / 3

        if g1 >= 7:
            print('Aprovado em G1')
        elif g1 < 4:
            print('Reprovado')
        else:
            try:
                g2 = float(input('Informe a nota do exame G2: '))
            except:
                print('Nota inválida!')
            
            if g2 < 0 or g2 > 10:
                print('Nota devem estar no intervalo de 0 a 10.')
            else:
                m = (g1 + g2) / 2

                if m < 5:
                    print('Reprovado em grau 2.')
                else:
                    print('Aprovado em grau 2.')