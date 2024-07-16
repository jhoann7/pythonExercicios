di = int(input("Quantos dias de aluguel: "))
km = float(input("Quantos KM rodados: "))
totd = di*60
totkm = km*0.15
tot = totd + totkm
print("O total a pagar é de R${:.2f}".format(tot))