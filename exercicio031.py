dis = float(input('Informe a distância da viagem em KM: '))

if dis > 200:
    print('O preço da sua passagem será R${:.2f}'.format(dis*0.45))
else:
    print('O preço da sua passagem será R${:.2f}'.format(dis*0.50))