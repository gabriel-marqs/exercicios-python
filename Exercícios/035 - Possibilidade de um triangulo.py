n1 = float(input('Informe o tamanho do primeiro lado: '))
n2 = float(input('Informe o tamanho do segundo lado: '))
n3 = float(input('Informe o tamanho do terceiro lado: '))

if (n1-n2) < n3 < n1+n2 and (n2-n3) < n1 < n2+n3 and (n1-n3) < n2 < n1+n3:
    print('Os 3 lados formam um triângulo!')
else:
    print('Os 3 lados não formam um triângulo!')