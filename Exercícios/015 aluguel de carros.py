d = int(input('Informe quantos por quantos dias o carro foi alugado: '))
km = float(input('Informe quantos km o carro percorreu: '))
vd = d*60
vk = km*0.15
vf = vd+vk

print('O valor a pagar referente a {} dias será de {:.2f}.\nO valor a pagar por {}kms será de R${:.2f}.\n'
      'O total a ser pago será de R${:.2f}.'.format(d, vd, km, vk, vf))
