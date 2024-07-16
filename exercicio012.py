pre = float(input("Qual é o preço do produto? R$"))
print("O produto que custava R${}, agora com desconto de 5% vai custar R${:.2f}".format(pre, pre -(pre/100)*5))