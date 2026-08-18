altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area = altura * largura
qtd_Tinta = area / 2

print("A área dessa parede é de {}m² e você vai precisar de {}L de tinta".format(area, qtd_Tinta))

