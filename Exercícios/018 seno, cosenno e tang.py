import math
a = float(input('Informe o ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo de {} tem o SENO {:.2f}\nO ângulo de {} tem o COSSENO {:.2f}\nO ângulo {} tem a TANGENTE {:.2f}.'
      .format(a, s, a, c, a, t))