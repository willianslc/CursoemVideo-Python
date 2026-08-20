"""
No caso aqui a variável "v" é um objeto e todo objeto tem suas
caracteriscas e realiza suas funcionalidades, eles tem
atributos e métodos, tudo que tiver esses parenteses no final como
o .isnumeric() são métodos, todos os objetos do tipo primitivo string
tem esses métodos mostrados e outros.
"""

v = (input("Digite algo: "))
print("O tipo primitivo do valor digitado é: ", type(v))
print("O valor digitado é númerico? ", v.isnumeric())
print("O valor digitado é alfabético? ", v.isalpha())
print("O valor digitado é alfanumerico? ", v.isalnum())
print("O valor digitado esta em maiúsculo? ", v.isupper())
print("O valor digitado esta em minúsculo? ", v.islower())
print("O valor digitado tem espaços? ", v.isspace())

