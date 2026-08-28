import random

nomes = []

for alunos in range(4):
    nomes.append(str(input("Digite o nome do aluno: ")))

escolhido = random.choice(nomes)

print("O aluno escolhido é {}".format(escolhido))