n = int(input("Digite um número: "))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print("O dobro do n° digitado é: {} \nO triplo é: {} \nE a raiz quadrada dele é: {:.2f}".format(dobro, triplo, raiz))

"""
VERSÃO DO PROFESSOR
n = int(input("Digite um número: "))
print("O dobro de {} vale {}.".format(n, (n * 2)))
print("O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.".format(n, (n * 3), n, (n**(1/2))))
"""