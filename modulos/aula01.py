"""
from math import sqrt, ceil ----> Isso aqui é o que chama de modulo\biblioteca
import math ----> Outra forma de chamar a biblioteca mas assim vem a biblioteca toda
num = int(input("Digite um número: "))
raiz = sqrt(num)

print("A raiz de {} é {:.2f}".format(num, ceil(raiz)))

Math é um biblioteca com algumas ferramentas matemáticas, seja para arredondar resultados para mais ou para menos
raiz quadrada, no caso sqrt é a raiz quadrada, ceil arredonda para cima, floor para baixo
"""
"""
import random #Importamos a biblioteca random, ela permite que a máquina gere números aleatórios
num = random.randint(1, 10) #Aqui pedimos para ele gerar um número inteiro aleatório de 1 a 10
print(num)

Se colocar da seguinte forma...
num = random.random() 
print(num)

Ele iria retornar um número qualquer que ele iria pegar na memória da máquina, porém dessa forma ele só gera
numeros aleatório entre 0 e 1
"""
