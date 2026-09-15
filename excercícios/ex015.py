#Mostra o valor inteiro de um número real

import math

num = float(input("Digite um numero real: "))

print("O número {} tem a parte inteira de {}".format(num, math.trunc(num)))