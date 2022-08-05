n = str(input('Informe seu nome completo: ')).strip().lower()
m = n.split()
print('Primeiro nome: {}\nÚltimo nome: {}'.format(m[0].title(), m[-1].title()))
