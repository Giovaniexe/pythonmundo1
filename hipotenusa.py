from math import hypot
print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo tetângulo,\n '
      'calcule e mostre o comprimento da hipotenusa \n')

# soma dos quadrados dos catetos é igual a porra da hipotenusa

co = float(input('Digite o tamanho do cateto oposto '))

ca = float(input('Digite o tamanho do cateto adjacente '))

h = hypot(co, ca)
print('O valor do cateto oposto é de {} e do cateto adjacente é de {} '
      'então o valor da hipotenusa é igual à: {: .2f}²\n \n'.format(co, ca, h))