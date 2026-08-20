dias = int(input("Por quantos dias vc alugou o carro? "))
km = float(input("Quantos km vc rodou com o carro? "))

calculo = dias * 60 + km * 0.15

print("Você irá pagar R${:.2f}".format(calculo))