v = float(input('Informe a quantos Km/h estava o veículo: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado no valor de R$ {:.2f}.'.format(m))
else:
    print('Você está dentro do limite de velocidade permitido.')
