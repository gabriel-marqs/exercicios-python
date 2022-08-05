f = str(input('Digite a frase: ')).strip().lower()
print('Sua frase possui {} letras A'.format(f.count('a')))
print(f.find('a')+1)
print(f.rfind('a')+1)