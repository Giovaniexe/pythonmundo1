import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('O senho de {} é {:.2f}' .format(angulo, seno))
cosseno = math.cos(math.radians((angulo)))
print('O seno de {} é igual à {:.2f}' .format(angulo, cosseno))
tangente = math.tan(math.radians((angulo)))
print('O seno {} é igual à {:.2f}' .format(angulo, tangente))
