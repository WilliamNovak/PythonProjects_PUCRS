# Receba o salário líquido e o número de dependetes e calcule os impostos e o salário líquido
try:
    sb = float(input('Informe o salário bruto: '))
except:
    print('Valor inválido!')

try:
    dep = int(input('Informe o número de dependentes: '))
except:
    print('Valor inválido!')

# Verifica faixa do INSS (aliquota e parcela)
if sb < 1212.01:
    ali_inss = 0.075
    parc_inss = 0
elif sb <= 2427.35:
    ali_inss = 0.09
    parc_inss = 18.18
elif sb <= 3641.03:
    ali_inss = 0.12
    parc_inss = 91
else:
    ali_inss = 0.14
    parc_inss = 163.82

# Calcula inss
inss = sb * ali_inss - parc_inss
# Verifica se nao passou do teto do inss
if inss > 828.39:
    inss = 828.39

print('INSS:',inss)

# Base para cálculo do IRRF
base = sb - inss - 189.59 * dep

if base <= 1903.98:
    ali_irrf = 0
    parc_irrf = 0
elif base <= 2826.65:
    ali_irrf = 0.075
    parc_irrf = 142.8
elif base <= 3751.05:
    ali_irrf = 0.15
    parc_irrf = 354.8
elif base <= 4664.68:
    ali_irrf = 0.225
    parc_irrf = 636.13
else:
    ali_irrf = 0.275
    parc_irrf = 869.36

# IRRF é a alíquota aplicada à base de cálculo, subtraída da parcela a deduzir
irrf = base * ali_irrf - parc_irrf

print('IRRF:',irrf)

sl = sb - inss - irrf
print('Salário Líquido:',sl)