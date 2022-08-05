n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
n3 = float(input('Informe um terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor é {} e o maior valor é {}.'.format(menor, maior))
