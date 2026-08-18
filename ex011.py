preco_Original = float(input("Digite o valor do produto: "))

calculo = (preco_Original * 5) / 100
preco_Final = preco_Original - calculo

print("O valor do desconto é R${:.2f} e o valor final do produto com desconto é R${:.2f}".format(calculo, preco_Final))