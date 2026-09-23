frase = str(input("Digite uma frase: "))

frase1 = frase.count('a')
print("Nessa frase temos {} letas A".format(frase1))

frase2 = frase.lower()
frase3 = frase2.find('a')
print("A primeira letra A parece na posição {}".format(frase3))

frase4 = frase2.rfind('a')
print("E a ultima vez que a letra A parece é na posição {}".format(frase4))