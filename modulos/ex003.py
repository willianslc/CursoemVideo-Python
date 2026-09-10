"""
3 - Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno
e tangente desse ângulo.
"""

#Qunado chamado as ferramentas da biblioteca Math dessa forma, não precisamos chamar elas assim Math.sin, dá erro
#from math import sin, cos, tan, radians
from math import radians, sin, cos, tan

angulo = float(input("Digite o valor do ângulo: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print("O valor de seno é {:.2f}, cosseno é {:.2f} e a tangente é {:.2f}".format(seno, cosseno, tangente))