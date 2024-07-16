s = float(input("Qual é o salário do funcionário? R$"))
print("Um funcionário que ganhava R${}, com 15% de aumento, passará a ganhar R${:.2f}".format(s, s +((s/100)*15)))