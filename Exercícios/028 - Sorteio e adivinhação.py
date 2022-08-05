import random
import time
s = random.randint(0, 5)
print('-=-'*20)
a = int(input('Estou pensando em um número de 0 a 5... tente adivinhar!\nR: '))
print('Será que você ganhou?')
time.sleep(4)
if s == a:
    print('Mas quem diria... você acertou!')
else:
    print('Hahaha... como eu previa, você errou. Estava pensando no número {}'.format(s))
print('-=-' * 20)
