altura = float(input("Digite a altura da parede em metros: "))
largura = float(input("Digite a largura da parede em metros: "))

area = altura * largura
qtd_Tinta = area / 2

print("A área dessa parede é de {:.2f}m² e você precisará de {:.1f}L de tinta para pintar essa parede".format(area, qtd_Tinta))

"""
VERSÃO DO PREFESSOR

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
área = larg * alt

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisará de {}L de tinta.".format(tinta))")
"""