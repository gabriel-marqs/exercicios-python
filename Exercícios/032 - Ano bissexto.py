from datetime import date
a = int(input('Informe o ano: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {} é um ano bissexto!'.format(a))
else:
    print('O ano {} NÃO é um ano bissexto!'.format(a))
