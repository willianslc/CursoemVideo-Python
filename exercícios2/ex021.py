nome = str(input("Digite o nome completo: "))

nomeMai = nome.upper()
nomeMin = nome.lower()
nomeSemEspaco = nome.replace(" ", "")
nomeCont = len(nomeSemEspaco)
lista_nome = nome.split()
lista_nome = len(lista_nome[0])

print(nomeMai)
print(nomeMin)
print(nomeSemEspaco)
print(nomeCont)
print(lista_nome)