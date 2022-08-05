n = float(input('Informe o valor do preço sem desconto: '))
d = n - (n*5/100)
print('R$ {:.2f} com 5% de desconto sai por {:.2f}'.format(n, d))
