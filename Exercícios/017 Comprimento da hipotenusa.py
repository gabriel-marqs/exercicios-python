from math import sqrt, hypot
a = float(input('Informe o comprimento do cateto oposto: '))
b = float(input('Informe o comprimento do cateto adjacente: '))
c = a**2 + b**2 # opção 1 #
d = sqrt(c) # opção 1 #
hi = hypot(a, b) # opção 2 #
print('O comprimento da hipotenusa é de {:.2f}'.format(d))
print('O comprimento da hipotenusa é de {:.2f}'.format(hi))