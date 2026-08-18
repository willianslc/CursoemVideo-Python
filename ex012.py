salario_Atual = float(input("Digite o valor do salário atual: "))

calculo = (salario_Atual * 15) / 100
salario_Aumento = salario_Atual + calculo

print("Você receberá R${:.2f} de aumento salarial, e o seu salário com aumento ficará no valor de R${:.2f}".format(calculo, salario_Aumento))