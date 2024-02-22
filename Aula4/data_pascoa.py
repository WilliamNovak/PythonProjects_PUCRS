# Calcular a data da Páscoa para um determinado ano entre 1900 e 2099
# Algoritmo fornece data em março, se passar limite considerar Abril
# Se ano for 1954, 1981, 2049 ou 2076 subtrair 7 dias da data
try:
    ano = int(input('Informe um ano entre 1900 e 2099: '))
except:
    print('Ano inválido!')

if ano < 1900 or ano > 2099:
    print('Ano deve ser entre 1900 e 2099.')
else:
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    dia = 22 + d + e

    if ano == 1954 or ano == 1981 or ano == 2049 or ano == 2076:
        dia = dia - 7
    
    if dia > 31:
        dia = dia - 31
        print('Páscoa dia',dia,'de abril')
    else:
        print('Páscoa dia',dia,'de março')