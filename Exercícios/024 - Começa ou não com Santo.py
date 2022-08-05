c = str(input('Informe o nome da cidade: ')).lower().strip()
d = c.split()
print('A cidade começa com Santo? ', 'santo' in d[0])