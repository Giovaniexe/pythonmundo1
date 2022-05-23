# 1 - FAÇA UM PROGRAMA QUE LEIA UMA NUMERO INTEIRO E MOSTRE SEU SUCESSOR E ANTECESSOR
# 2 - CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O DOBRO TRIPLO E RAIZ QUADRADA DESSE NUMERO
# 3 - DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A MEDIA
# 4 - ESCREVA UM PROGRAMA QUE LIA UM VALOR EM METROS E EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS
# 5 - FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA SUA TABUADA
# 6 - CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
''' 7 - FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE
TINTA NECESSÁRIO PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2m²'''
# 8 - FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO VALOR COM 5% DE DESCONTO
# 9 - FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO

print('FAÇA UM PROGRAMA QUE LEIA UMA NUMERO INTEIRO E MOSTRE SEU SUCESSOR E ANTECESSOR')
numero = int(input('digite um numero '))
s = numero + 1
a = numero - 1
print('o numero {} é o sucessor do {} e antecessor do {}'.format(numero, a, s))

print('\n', '\n')

print('CRIE UM ALGORITIMO QUE LEIA UM NUMERO E MOSTRE O DOBRO, TRIPLO E RAIZ QUADRADA DESSE NUMERO')
n = int(input('digite um numero '))
print('O drobro do numero {} é {} '.format(n, n * 2))
print('O triplo do numero {} é {} '.format(n, n * 3))
print('A raiz quadrada de de {} é {}'.format(n, n ** 0.5))

print('\n', '\n')

print('DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE A MEDIA')
nota1 = float(input('digite a primeira nota '))
nota2 = float(input('digite a segunda nota '))
print('A média das notas é: {}'.format((nota1 + nota2) / 2))

print('\n', '\n')

print('ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS')

print('\n', '\n')

metros = float(input('Digite quantos metros você tem: '))
print(
    'se voce tem {0} metros, logo você tem {1} centimetros e em milimetros você mede {2} '.format(metros, metros * 100,
                                                                                                  metros * 1000))

print('\n', '\n')

print('FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA SUA TABUADA')

print('\n', '\n')

tabuada = int(input('digite o numero da tabuada '))
print(tabuada, 'x 1 = ', tabuada * 1, '\n', tabuada, 'x 2 = ', tabuada * 2, '\n', tabuada, 'x 3 = ', tabuada * 3, '\n',
      tabuada, 'x 4 = ', tabuada * 4, '\n', tabuada, 'x 5 = ', tabuada * 5, '\n', tabuada, 'x 6 = ', tabuada * 6, '\n',
      tabuada, 'x 7 = ',
      tabuada * 7, '\n', tabuada, 'x 8 = ', tabuada * 8, '\n', tabuada, 'x 9 = ', tabuada * 9, '\n', tabuada, 'x 10 = ',
      tabuada * 10)

print('\n', '\n')

print('CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR')

print('\n', '\n')

dinheiro = float(input('quanto de dinheiro em real você tem na sua carteira? R$. '))
cambio = dinheiro / 4.86
print('Você pode comprar o equivalente à U$ {:.2f}'.format(cambio))

print('\n', 'FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSÁRIO PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2m²')

w = float(input('Digite a largura da parede '))
h = float(input('Digite a Altura da parede '))
tinta = (w * h) / 2
print('\n', 'A sua parede possui {0}M², sendo assim você irá precisar de {1} litro(s) de tinta'.format(w * h, tinta))

print('\n', 'FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO VALOR COM 5% DE DESCONTO')
valor_real = float(input('Digite o valor do produto R$. '))
valor_descontado = valor_real * 0.05
print('O Valor do produto com o desconto fica R$. {}'.format(valor_real - valor_descontado))

print('\n', 'FAÇA UM ALGORITIMO QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO')

salario = float(input('Qual o antigo salário? '))
novo_salario = salario * 0.15
print('O aumento do salario desse colaborador é de {0} e ele passará a receber ao todo {1}' .format(novo_salario, salario+novo_salario))

print('ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM Cº PARA ºF')
c = float(input('Digite a temperatura em celsius'))
f = ((9*c)/5+32)
print('A temperatura convertida fica {}º' .format(f))
