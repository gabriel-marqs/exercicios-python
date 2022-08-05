l = float(input('Informe a largura da parede em metros: '))
a = float(input('Informe a altura da parede em metros: '))
m = l*a
t = m/2
print('Em uma área de {:.2f}m², será necessário {:.2f} litros de tinta.'.format(m, t))
