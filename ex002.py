#TIPOS PRIMITIVOS

"""
O int ali é um dos 4 tipos primitivos,
converte o número de string(texto) para número
que o python consiga calcular se não colocar o int
o python entende que o número que o usuário digitar é um texto e
assim não faz a soma dá erro, pois por padrão o input sempre
considera tudo que o usuário digita como texto
por isso temos que colocar o int para fazer a conversão.

EXPLICANDO OS TIPOS PRIMITIVOS:

INT - 7, -4, 0, 9875 -> Seja o número negativo ou positivo se não tem ponto/vírgula nele então é int(inteiro)
FLOAT - 4.5, 0.0075, -15.223, 7.0 -> Todos que tiver o ponto ou vírgula são float(n° real)
BOOL - True/False -> Esse é para situações logicas, sim ou não, verdadeiro ou falso
STR - "Olá", "O resultado da soma..." -> Esse representa tudo o que for String(texto)
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2

print("O resultado da soma dos numeros é {}".format(soma))



