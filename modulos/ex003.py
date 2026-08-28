from math import sin, cos, tan, radians
#Qunado chamado as ferramentas da biblioteca Math essa forma, não precisamos chamar elas assim Math.sin, dá erro

angulo = float(input("Digite o valor do ângulo em graus: "))
radians(angulo)
seno = sin(angulo)
cosseno = cos(angulo)
tangente = tan(angulo)

print("O valor de seno é {:.3f}, cosseno é {:.3f} e a tangente é {:.3f}".format(seno, cosseno, tangente))