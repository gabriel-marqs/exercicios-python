n = float(input('Informe a distância da viagem em Km: '))
if n <= 200:
    c = n*0.5
else:
    c = n*0.4
print('O valor da viagem custará R$ {}.'.format(c))