from random import choice
a1 = input("Nome do primeiro aluno: ")
a2 = input("Nome do segundo aluno: ")
a3 = input("Nome do terceiro aluno:")
a4 = input("Nome do Quarto aluno:")

lista = [a1, a2, a3, a4]

ale = choice(lista)

print("O escolhido para apagar o quadro foi {} ".format(ale))