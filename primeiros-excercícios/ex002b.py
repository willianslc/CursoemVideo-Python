#Continuação do ex002
"""
O bool só retorna verdadeiro ou falso, por tanto se
o usuário digitar um valor ele vai retornar True, pois o valor foi digitado
mas se o usuário não digitar nada apenas apetar Enter, ele retorna False, pois "n"
ficou vazio/null

EXEMPLO 1
vemos o método "isnumeric" onde ele
te retorna se o valor digitado é numerico ou não, se for é True
se não é False. Caso seja digitado letra e numero prevalecerá o False

EXEMPLO 2
O método "isalpha" diz se é letra ou não
se digitar letra e número retorna False, pois letra e número
são alfa-numerico, para letra e numero existe o método
"isalphanum".
"""

#Exemplo 1
n1 = bool(input("Digite um valor: "))
print(n1)

#Exemplo 2
n2 = input("Digite qualquer coisa: ")
print(n2.isnumeric())

#Exemplo 3
n3 = input("Digite qualquer coisa: ")
print(n3.isalpha())