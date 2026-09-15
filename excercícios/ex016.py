"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""
from math import sqrt

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = sqrt(cateto_oposto**2 + cateto_adjacente**2)

print("O comprimento da hipotenusa desse triângulo retângulo é {:.2f}".format(hipotenusa))

"""
Outra forma de fazer com outra propriedade da biblioteca math:
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
A propriedade hypot já é o proprio calculo da hipotenusa
"""