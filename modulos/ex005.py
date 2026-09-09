import random

nomes = []

for alunos in range(4):
    nomes.append(str(input("Digite o nome do aluno: ")))

random.shuffle(nomes) # O Shuffle não usa variável, pois ele não cria nada dentro da váriavel nomes, ele apenas embaralha

print("O aluno escolhido é {}".format(nomes))