s = float(input('Informe o salário: '))
if s > 1250:
    a = s*1.1
    print('Você receberá um aumento de 10%. Seu salário será de R$ {:.2f}.'.format(a))
else:
    a = s*1.15
    print('Você receberá um aumento de 15%. Seu salário será de {:.2f}'.format(a))