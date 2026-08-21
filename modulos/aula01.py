import random #Importa a biblioteca toda

from math import sqrt, ceil, floor #Importa só o que vai usar
num1 = int(input("Digite um número: "))
raiz = sqrt(num1) #SQRT faz raíz quadrada nesse caso

num2 = random.random() #Gera número aleatório entre 0 e 1
print(num2)

num3 = random.randint(1, 10) #Pega um número "inteiro" aleatório entre 1 e 10
print(num3)