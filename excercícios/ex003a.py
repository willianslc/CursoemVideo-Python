#Operadores Aritiméticos
"""
ORDEM DE PRECEDÊNCIA
Em caso de uma expressão aritimética o que começa sendo resolvido primeiro pelo Python?

1) () → Sempre comneça resolvendo o que tiver dentro dos parenteses
2) ** → Segunda coisa a ser resolvida é as potências
3) * / // % → Aqui não tem uma ordem, resolve o que vir primeiro
4) + - → Por último resolve esses
"""

#n1 = int(input("Um valor: "))
#n2 = int(input("Outro valor: "))
#print("A soma vale {}".format(n1 + n2))

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(soma, multiplicacao, divisao), end=" ")
print("Divisão inteira é {} e a potência é {}".format(divisao_inteira, exponenciacao))