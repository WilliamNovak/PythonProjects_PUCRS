# Receba o mês e informe quantos dias tem
try:
    m = int(input('Informe o mês do ano (1-12): '))
    a = int(input('Informe o ano: '))
except:
    print('Valor inválido!')

if m < 1 or m > 12:
    print('Mês deve estar entre 1 e 12.')
else:
    if m == 2:
        if (a%400 == 0) or (a%4 == 0 and a%100 != 0):
            d = 29
        else:
            d = 28
    elif m == 4 or m == 6 or m == 9 or m == 11:
        d = 30
    else:
        d = 31

    print('Total de dias do mês:',d)