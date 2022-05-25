from random import choice, shuffle

print('Um professor quer sortear um dos seus 4 alunos para apagar o quadro.'
      'faça um programa que ajude ele, lendo o nomede deles e escrevendo o nome do escolhido')

n1 = str(input('Digite o nome do primeiro aluno '))
n2 = str(input('Digite o nome do segundo aluno '))
n3 = str(input('Digite o nome do terceiro aluno '))
n4 = str(input('Digite o nome do quarto aluno '))

lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))

print('__________________________________________________')

print('o mesmo professor agora deseja sortear a ordem'
      'de apresentação dos trabalhos dos 4 alunos, escreva o programa')
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))




