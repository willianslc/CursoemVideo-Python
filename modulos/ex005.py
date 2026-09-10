"""
5 - O mesmo professor do desafio anterior quer sortear a ordem
de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

import random

nomes = []

for alunos in range(4):
    nomes.append(str(input("Digite o nome do aluno: ")))

random.shuffle(nomes) # O Shuffle não usa variável, pois ele não cria nada dentro da váriavel nomes, ele apenas embaralha

print("O aluno escolhido é {}".format(nomes))

"""
VERSÃO DO PROFESSOR SIMPLIFICADA:
from random import shuffle

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)

print('0 aluno escolhido foi {}'.format(escolhido))
"""